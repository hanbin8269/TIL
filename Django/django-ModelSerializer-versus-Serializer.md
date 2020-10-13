# `ModelSerializer` VS `Serializer`
지금까지 뭘 만들때마다 `ModelSerializer`를 사용하여 만들었는데, 로그인을 구현하다가 
```json
{
  "email": [
    "user with this email address already exists."
  ]
}
```
라는 예외를 발견했다. 원래 회원가입을 구현할때 나와야 하는 예외인데, 로그인에서 나와서 당황했다.
```python
# 이 코드에서 예외가 검출되었다.

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        credentials = {"email": data["email"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            payload = {
                "id": user.id, 
                "email": user.email, 
            }

            token = utils.jwt_encode_handler(payload)

            return (user, token)

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)
```

[django-rest-framework 깃허브 serializers.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py) 의 `ModelSerializer` 와 `Serializer` 클래스를 비교해보면 `ModelSerializer`은 `Serializer`를 상속받아 `create` , `update` 등의 메서드를 오버라이딩하고 여러 메서드를 추가한 형태이다.
```python
class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    # 이것들은 declared_fields에 들어가게 된다

    class Meta:
        model = User
        fields = ("email", "password")

    def validate(self, data):
        credentials = {"email": data["email"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            payload = {"id": user.id, "email": user.email}

            token = utils.jwt_encode_handler(payload)

            return (user, token)

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)
```
그런데 이렇게 바꿔주면 해결이 된다. 그 이유가 뭘까?
```python
# rest_framework/utils/field_mapping.py
class ModelSerializer(Serializer):
    ...
    def get_fields(self):
        ...
        for field_name in field_names:
            # If the field is explicitly declared on the class then use that.
            if field_name in declared_fields: # 여기
                fields[field_name] = declared_fields[field_name]
                continue

            extra_field_kwargs = extra_kwargs.get(field_name, {})
            source = extra_field_kwargs.get("source", "*")
            if source == "*":
                source = field_name

            # Determine the serializer field class and keyword arguments.
            field_class, field_kwargs = self.build_field(source, info, model, depth)
            # Include any kwargs defined in `Meta.extra_kwargs`
            field_kwargs = self.include_extra_kwargs(field_kwargs, extra_field_kwargs)
            # Create the serializer field.
            fields[field_name] = field_class(**field_kwargs)
    ...
```
`if field_name in declared_fields`에서 내가 선언했던 `email`,`password` 필드를 `fields[field_name] = declared_fields[field_name]`으로 `fields`변수에 넣고 continue를 했기 때문에 `build_field()`메서드가 실행되지 않아 Meta에서 만든 변수가 적용되지 않았던 것이다.
만약 `build_field()`메서드가 실행된다면,
`build_field()` -> `build_standard_field()` -> `get_field_kwargs()` 에서
```python
# rest_framework/utils/field_mapping.py

def get_field_kwargs(field_name, model_field):
    ...
    if getattr(model_field, "unique", False):
        unique_error_message = model_field.error_messages.get("unique", None)
        if unique_error_message:
            unique_error_message = unique_error_message % {
                "model_name": model_field.model._meta.verbose_name,
                "field_label": model_field.verbose_name,
            }
        validator = UniqueValidator(
            queryset=model_field.model._default_manager, message=unique_error_message
        )
        validator_kwarg.append(validator)
    ...
```
함수를 실행하여 `unique=True`인 필드의 `validator`를 `UniqueValidator`로 지정하여 줄 것이다.
```python
# rest_framework/validators.py

class UniqueValidator:
  ...

  def __call__(self, value, serializer_field):
    # Determine the underlying model field name. This may not be the
    # same as the serializer field name if `source=<>` is set.
    field_name = serializer_field.source_attrs[-1]
    # Determine the existing instance, if this is an update operation.
    instance = getattr(serializer_field.parent, "instance", None)

    queryset = self.queryset
    queryset = self.filter_queryset(value, queryset, field_name)
    queryset = self.exclude_current_instance(queryset, instance)
    if qs_exists(queryset):
        raise ValidationError(self.message, code="unique")
  ...
```
위와 같이 `UniqueValidator`는 `unique = True` 속성이 붙은 값들은 중복을 걸러주는 역할을 하는데 한다.


------------
## 결론

`ModelSerializer`의 `get_fields()`메서드에서 `build_field()` -> `build_standard_field()` -> `get_field_kwargs()`의 순서로 메서드를 실행 시켜 미리 필드를 선언하지 않고 Meta클래스에 `fields = ("email")`같은 형태로 넣었다면 필드 `validator`에 `UniqueValidator`가 추가되어 중복을 허용하지 않게 된다.