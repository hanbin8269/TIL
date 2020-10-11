# Python dir / hasattr / getattr / setattr

## `dir(object)`
`object` 객체에 어떤 변수와 메서드가 있는지 나열한다.
```python
class Test():
    def __init__(self):
        self.aaa = 1
        self._bbb = 2
        self.__ccc = 3
    
    def hello(self):
        print('hello')

t = Test()
print(dir(t))
# ['_Test__ccc', '__class__', '__delattr__', '__dict__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', '_bbb', 'aaa', 'hello']
```
보면 여러가지 사용가능한 메서드들과 변수들이 있다.
또한 `self.__ccc` 는 `_Test__ccc`로 바뀌어 있는 것도 볼 수 있다.
## `hasattr(object, str : name)`
`object` 에 `name`이라는 이름을 가지고 있는 변수 또는 메서드가 있는지 `boolean` 값으로 반환해 준다.
```python
class Test():
    def __init__(self):
        self.aaa = 1
        self._bbb = 2
        self.__ccc = 3
    def hello(self):
        print('hello')

t = Test()
        
print(hasattr(t,'aaa')) # True
print(hasattr(t,'__class__')) # True
print(hasattr(t,'_Test__ccc')) # True
print(hasattr(t,'nonono')) # False
```

## `getattr(object, str : name)`
`object`에 `name` 이라는 이름을 가지고 있는 속성의 값을 가져온다
```python
class Test():
    def __init__(self):
        self.aaa = 1
        self._bbb = 2
        self.__ccc = 3
    
    def hello(self):
        print('hello')

t = Test()

print(getattr(t, 'aaa')) # 1
print(getattr(t, 'hello')) # <bound method Test.hello of <__main__.Test object at 0x000001DA82D90668>>
```

## `setattr(object, str : name, value)`
`object`에 `name`이라는 이름을 가지고 있는 속성의 값을 `value`로 변경한다.
```python
class Test():
    def __init__(self):
        self.aaa = 1
        self._bbb = 2
        self.__ccc = 3
    
    def hello(self):
        print('hello')

t = Test()

setattr(t,'aaa',123)
print(t.aaa) # 123


def callback():
    print('goodbye :)')

setattr(t,'hello',callback)
t.hello() # "goodbye :)"
```
----------

이 내장함수들은 `DRF`와 같은 오픈소스를 볼때 자주 눈에 띄었는데 뭔지 잘 몰라서 코드 이해에 어려움이 있었다.
이제 소스코드 이해능력이 조금은 늘게 된거같다