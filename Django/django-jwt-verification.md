# Django JWT 인증 방식
Django로 JWT를 이용한 유저 인증을 구현하려고 한다.
`restframework-jwt` 라이브러리를 사용하면 간단히 구현할 수 있지만 자존심이 상한다. 
공부하는겸 직접 구현해보자.

## 1. User Model
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
```
django에서 기본으로 제공하는 User 모델은 내가 원하는 모양과 달라서 커스텀을 해주었다.
```python
AUTH_USER_MODEL = "account.User" # "앱.모델이름"
```
그럼 `settings.py` 또는 `base.py`에 위 내용을 추가시켜준다.
저 내용을 추가하면 django에서 제공하는 `authenticate()`와 같은 메서드에서 내가 만든 모델로 인증을 처리해준다.

## 2. Serializer
회원가입, 로그인을 처리하기 위해 `CreateSerializer`, `LoginSerializer` 두개를 만들어 줄것이다. 또한 Response할때 json으로 직렬화 해줄 `UserSerializer`도 만들어 줄것이다.
```python
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _
import jwt


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        credentials = {"email": data["email"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            return user

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
```
여기서 jwt 인증을 처리하기 위해서는 `LoginUserSerializer`에 몇가지를 추가해줘야 한다.

## 3. JWT 인증 추가하기
이 글을 쓴 이유다.
`restframework-jwt`의 `utils.py` 코드를 보면 `jwt_encode_handler`메서드가 있다.
```python
# rest_framework_jwt\utils.py
...
def jwt_encode_handler(payload):
    key = api_settings.JWT_PRIVATE_KEY or jwt_get_secret_key(payload)
    return jwt.encode(
        payload,
        key,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')
```
JWT 인코딩을 해주는 메서드다. 이걸 사용해서 만들어보자

```python
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _ # 추가 (지역에 맞춰 각국의 언어로 번역해주는 라이브러리라고 한다. 공부해봐야겠다)
import jwt # 추가

class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        credentials = {"email": data["email"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            payload = {"id": user.id, "email": user.email, "username": user.username} # token에 넣을 값 생성

            token = utils.jwt_encode_handler(payload) # encode

            return (user, token)

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)
```
여기서 사용된 `authenticate` 메서드를 쓰기 위해서는 `base.py` 또는 `settings.py`에 `AUTHENTICATION_BACKENDS`를 추가해줘야 한다.
```python
# base.py or settings.py
    ...
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Django가 관리하는 AUTH
]
```
## 4. View 
```python
from rest_framework import generics, status
from .serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer
from rest_framework.response import Response

class RegistrationView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["password"]) < 6:
            message = {"message": "password is too short"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({"user": UserSerializer(user).data})


class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data

        return Response({"user": UserSerializer(user).data, "token": token})
```
여기서 `serailizer.validated_data`에 어떻게 값이 들어가는지 궁금해서 코드를 봤더니
```python
# restframework/serializers.py

def is_valid(self, raise_exception=False):
    assert hasattr(self, "initial_data"), (
        "Cannot call `.is_valid()` as no `data=` keyword argument was "
        "passed when instantiating the serializer instance."
    )

    if not hasattr(self, "_validated_data"):
        try:
            self._validated_data = self.run_validation(self.initial_data)
        except ValidationError as exc:
            self._validated_data = {}
            self._errors = exc.detail
        else:
            self._errors = {}
        
    if self._errors and raise_exception:
        raise ValidationError(self.errors)
    return not bool(self._errors)

@property
def validated_data(self): # validated_data getter
    if not hasattr(self, "_validated_data"):
        msg = "You must call `.is_valid()` before accessing `validated_data`."
        raise AssertionError(msg)
    return self._validated_data
```
`is_valid`메서드를 실행하면 `self._validated_data`에 리턴값을 넣어주는데, `@property` 데코레이터를 사용해서 getter를 만들어 놨다