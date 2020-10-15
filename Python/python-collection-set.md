# Collection - set

## Set?
set은 파이썬에서 사용하는 자료형이다. 특징으로는 **순서가 없으며**, **중복을 허용하지 않는다**.
set자료형은 아래와 같이 만든다.
```python
a = {1,2,3,4,5}
```
또한 아래와 같이 변환할 수 있다.
```python
a = set([1,2,3])
b = set('hello set')

print(a)
# {1, 2, 3}
print(b)
# {'s', 'h', 'e', 'o', 't', 'l', ' '} # l의 중복이 허용되지 않았다
```
아래와 같은 형태라면 오류가 발생할 수 있다.
```python
a = {1,2,3,4,5}
b = set([1,2,3,4,5])

c = set([1,2,[3,4],5])
# TypeError: unhashable type: 'list'
```

## 합집합, 교집합, 차집합
```python
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
```
```python
a | b # 합집합
# {1,2,3,4,5,6,7,8,9,10}

a & b # 교집합
# {4,5,6}

a - b # 차집함 01
# {1,2,3}
b - a # 차집합 02
# {7,8,9,10}
```
위와같이 만들수도 있다.

## 값 추가, 여러개 추가, 제거
```python
a = {1,2,3,4,5,6}

# 값 추가
a.add(7)

# 값 여러개 추가
a.update([8,9,10,11])

# 값 제거
a.remove(10)
```

## 활용
```python
# rest_framework/serializers.py

...

if fields is not None:
    required_field_names = set(declared_fields)

    for cls in self.__class__.__bases__:
        required_field_names -= set(getattr(cls, '_declared_fields', []))
    for field_name in required_field_names:
        assert field_name in fields, (
            "The field '{field_name}' was declared on serializer "
            "{serializer_class}, but has not been included in the "
            "'fields' option.".format(
                field_name=field_name,
                serializer_class=self.__class__.__name__
            )
        )
    return fields
```
위와 같이 `list`를 중복없이 사용하고 싶을때 자주 사용하는 듯 하다.