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


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data): # 여기서 JWT를 처리할거다
        user = authenticate(**data)
        if user and user.is_active:
            return user # JWT를 추가한다면, (user,token)으로 튜플로 넘겨줄 것이다
        raise serializers.ValidationError("Unable to login with provided credentials")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
```
근데 여기서 jwt 인증을 처리하기 위해서는 `LoginUserSerializer`에 몇가지를 추가해줘야 한다.

## 3. JWT 인증 추가하기
이 글을 쓴 이유이자 본론이다.
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

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def _check_payload(self, token): # 만든 token이 유효한지 확인해 준다
        try:
            payload = utils.jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _("Signature has expired.")
            raise serializers.ValidationError(msg)
        except jwt.DecodeError:
            mas = _("Error decoding signature.")
            raise serializers.ValidationError(msg)

        return payload

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            token = utils.jwt_encode_handler(user)

            self._check_payload(token) 

            return (user, token) # 튜플로 보내주자

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)
```
만든 token에 이상이 있으면 안되기 때문에 메서드를 하나 추가해 주었다.

## 4. View 
view는 내일 써야겠다.