# 파이썬 메타클래스란?

메타클래스에 대해 알아보기 이전에 파이썬의 데이터 모델에 대한 이해가 필요하다.

파이썬에서 모든 것은 데이터를 추상화 한 객체로 이루어져 있다.
또한, 파이썬의 객체는 아이덴티티, 값, 타입을 가지고 있다.

#### 아이덴티티 (`id`)
**`id()`** 함수를 통해 얻을 수 있으며 객체의 수명동안 유일하고 불변함이 보장되는 정수다.
#### 값 (`value`)
객체의 타입에 따라 불변할 수 있고 가변할 수도 있다. `ex)tuple : 불변, list : 가변`
#### 타입 (`type`)
객체가 지원하는 연산들과 그 타입의 객체가 가질 수 있는 값(`ex) int : 1, list : [1,2]`)들을 통해 객체의 특성을 정의한다. 객체의 타입은 `type()`을 통해 얻을 수 있으며, 불변하다.

여기서 말한 타입과 같이 파이썬의 모든 객체들은 어떠한 타입에 의해 정의된다.

파이썬의 `type()` 빌트인 함수를 사용하면 객체의 타입을 알 수 있다.
```python
class Test:
    pass
t = Test()
type(t)
# <class '__main__.Test'>

def hello():
    pass
type(hello)
# <class 'function'>

type(1)
# <class 'int'>
```
위 예제를 보면 `Test` 클래스의 인스턴스인 `t`는 `Test`가 타입이고, `hello` 함수는 `function`이 타입이며, 1 정수는 `int`가 타입이다.

그렇다면, `Test` 클래스의 타입은 무엇일까?
```python
class Test:
    pass
type(Test)
# <class 'type'>
```
놀랍게도, `Test` 클래스 객체의 타입이 존재한다.
여기서 출력된 `type`을 `Test` 클래스의 **메타 클래스**라고 한다.

메타클래스는 클래스를 인스턴스로 가진다.
그러면 메타클래스는 무슨 용도로 사용하는 걸까?

그전에 몇가지 메타클래스의 매직 메소드에 대해 알아보자
```python
class TestMeta(type):
    def __prepare__(mcs, *args, **kwarg): # 메타 클래스가 결정되었을 때 (mro가 구성된 후) 클래스 정의를 위해 호출된다.
        # mcs = metaclass
        print("__prepare__()")
        return super.__prepare__(mcs, *args, **kwarg)
    
    def __new__(mcs, *args, **kwargs):  # 클래스를 생성 할 때 호출됨
        # mcs = metaclass
        print("__new__()")
        return super().__new__(mcs, *args, **kwargs)
    
    def __init__(cls, *args, **kwargs):  # 클래스가 생성 된 후 호출됨
        print("__init__()")
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):  # 클래스의 인스턴스를 생성할 때 호출됨
        print("__call__()")
        return super().__call__(*args, **kwargs)


class Test(metaclass=TestMeta):
    pass

# __prepare__()
# __new__()
# __init__()

t = Test()
# __call__()
```
위 코드를 보면 `__prepare__`, `__new__`, `__init__`, `__call__` 메소드를 작성하고 사용하는 것을 볼 수 있다.
`__prepare__` 메소드는 메타 클래스가 결정되었을 때 호출되며, 클래스의 네임 스페이스를 준비한다.
`__new__` 메소드는 클래스 객체를 생성 할 때 호출되며, `__init__` 메소드는 클래스가 생성 된 후 호출되어 클래스를 초기화 한다.
또한 `__call__` 메소드는 클래스의 인스턴스를 생성 할 때 호출 된다.

이 매직 메서드를 가지고 무슨 일을 할 수 있을까?

### 싱글톤 패턴 구현
싱글톤 패턴은 클래스의 인스턴스화를 항상 하나의 개체로만 제한하는 설계 패턴이다.
구현해 보자면
```py
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass

sl1 = SingletonClass()
sl2 = SingletonClass()

print(id(sl1))
# 1877212284048
print(id(sl2))
# 1877212284048
```
인스턴스 생성에 관여하는 `__call__()`메소드를 오버라이딩 해서 클래스를 key로 두고 인스턴스를 value로 만들어 클래스당 하나의 인스턴스를 가지도록 했다.

### 애트리뷰트 검증
DRF의 ModelSerializer 에는 내부 Meta 클래스가 없다면 오류를 일으킨다. 이에 대한 오류 검증을 DRF에서는 get_fields() 메소드에 구현해 두었는데, 이를 메타 클래스로 검증 할 수 있을 것 같다.
```python
def get_fields(self):
    ...

    assert hasattr(self, 'Meta'), (
        'Class {serializer_class} missing "Meta" attribute'.format(
            serializer_class=self.__class__.__name__
        )
    )
    ...
```
위 코드는 클래스 내부에 Meta 애트리뷰트가 있는지 확인하는 코드이다. 이를 메타클래스로 검증하는 코드를 짜보자
```python
class ModelSerializerMetaclass(SerializerMetaclass):
    def __new__(mcs, *args, **kwargs):
        name, bases, namespace = args
        if name not in ("ModelSerializer","HyperlinkedModelSerializer"):
            mcs._check_meta(name,namespace)

        return super().__new__(mcs, *args, **kwargs)

    def _check_meta(name,namespace):
        if not namespace.get("Meta", None):
            raise Exception(f'Class {name} missing "Meta" attribute')
        return


class ModelSerializer(Serializer, metaclass=ModelSerializerMetaclass):
    pass
```