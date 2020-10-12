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

[django-rest-framework 깃허브 serializers.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py) 의 `ModelSerializer` 와 `Serializer` 클래스를 비교해보면 `ModelSerializer`은 `Serializer`를 상속받아 `create` , `update` 등의 메서드를 오버라이딩한 형태이다.

`rest_framework/serializers.py` 를 보면 
```python
# rest_framework/serializers.py

class ModelSerializer(Serializer):

    serializer_field_mapping = {
        models.AutoField: IntegerField,
        models.BigIntegerField: IntegerField,
        models.BooleanField: BooleanField,
        models.CharField: CharField,
        models.CommaSeparatedIntegerField: CharField,
        models.DateField: DateField,
        models.DateTimeField: DateTimeField,
        models.DecimalField: DecimalField,
        models.DurationField: DurationField,
        models.EmailField: EmailField, # 여기!
        models.Field: ModelField,
        models.FileField: FileField,
        models.FloatField: FloatField,
        models.ImageField: ImageField,
        models.IntegerField: IntegerField,
        models.NullBooleanField: BooleanField,
        models.PositiveIntegerField: IntegerField,
        models.PositiveSmallIntegerField: IntegerField,
        models.SlugField: SlugField,
        models.SmallIntegerField: IntegerField,
        models.TextField: CharField,
        models.TimeField: TimeField,
        models.URLField: URLField,
        models.UUIDField: UUIDField,
        models.GenericIPAddressField: IPAddressField,
        models.FilePathField: FilePathField,
    } 

    ...
```
가 있는데,
```python
# rest_framework/serializers.py

class Serializer(BaseSerializer, metaclass=SerializerMetaclass):
  ...

  def to_internal_value(self, data):  # check!
          """
          Dict of native values <- Dict of primitive datatypes.
          """
          if not isinstance(data, Mapping):
              message = self.error_messages["invalid"].format(
                  datatype=type(data).__name__
              )
              raise ValidationError(
                  {api_settings.NON_FIELD_ERRORS_KEY: [message]}, code="invalid"
              )

          ret = OrderedDict()
          errors = OrderedDict()
          fields = self._writable_fields
          

          # 여기서 부터
          for field in fields:
              validate_method = getattr(self, "validate_" + field.field_name, None)
              primitive_value = field.get_value(data)
              try:
                  validated_value = field.run_validation(primitive_value) # 여기!
                  if validate_method is not None:
                      validated_value = validate_method(validated_value)
              except ValidationError as exc:
                  # exc : <UniqueValidator(queryset=User.objects.all())>
                  errors[field.field_name] = exc.detail
              except DjangoValidationError as exc:
                  errors[field.field_name] = get_error_detail(exc)
              except SkipField:
                  pass
              else:
                  set_value(ret, field.source_attrs, validated_value)
          # 여기까지 잘 보자

          if errors:
              raise ValidationError(errors)

          return ret

      ...
```
표시해둔 부분을 보면 field들이 `run_validation(primitive_value)`을 수행하는데, 이중에 `EmailField`도 있다.
오류나는 부분은 `<UniqueValidator(queryset=User.objects.all())>`에서 검출된 부분이다.


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
위와 같이 `unique = True` 속성이 붙은 값들은 모두 걸러주는 역할을 하는데, 여기서 걸리나보다.

------------
## 결론

`ModelSerializer`를 쓰면 `EmailField`를 가져오기 때문에 `UniqueValidator`를 처리하기 때문에 오류가 걸리게 된다