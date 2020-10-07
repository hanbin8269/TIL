# 파이썬에서의 언더스코어(_) 사용 방법
코드를 작성하기 위해 여러 예제들을 구경하다 보면 언더바가 여러 용도로 사용되는 것을 자주 볼 수 있다. 
그 사용방법 들을 정리해보자

## 1. 값을 무시할때
1,2,3 을 튜플로 리턴하는 함수가 있다.
```python
def get_foo():
    return (1,2,3)

# 여기서 1과 3만 가져오고 싶다. 그러면 일케 쓰면 된다

a,_,b = get_foo()
# a = 1, b = 3
```
그리고 또 여기 1부터 5까지 튜플로 리턴하는 함수가 있다.
```python
def get_foo():
    return (1,2,3,4,5)

# 만약 여기서 1과 5만 가져오고 싶다면 일케 쓰면 된다

a,*_,b = get_foo()
# a = 1, b = 5
```

##### 이처럼 쓸모없는 값을 무시할때 사용하는 문법이다
```python
for _ in range(10):
    print(1)
```
위와 같이 index가 쓸모없는 for문을 작성할 때도 사용된다

---
## 2. 특별한 값을 주고 싶을때

### 1. `_single_leading_underscore` : 한 모듈 안에서만 사용하는 private 클래스/함수/변수/메서드를 선언할 때 쓰는 컨벤션 
```python
_iternal_name = 'one_module'
```
일케 써두면 후에 `from module import *` 을 했을때 임포트에서 무시된다
```python
# example 01
def _is_extra_action(attr):
    return hasattr(attr, 'mapping')

# example 02
def __init__(self,url):
    self._url = url
    self._html = requests.get(url).text
    self._soup = BeautifulSoup(self._html, 'html.parser')
```
### 2. `single_trailing_underscore_` : 파이썬 키워드 들과 충돌을 피하기 위해 사용하는 컨벤션
```python
# example 01
icon_soup = self._soup.find('div', class_="asdfag")

# example 02
_list = [1,3,4]
```

##### 3. `__double_leading_underscore` : 하위 클래스에서 이름 충돌을 피하기 위해 만들어진 문법
이 문법은 `맹글링(mangling)`을 하여 파이썬 인터프리터가 속성 이름을 다시 쓰도록 한다.
```python
#example 01
class Test:
    def __init__(self):
        self.__a = 1

t = Test()
dir(t)
# ['_Test__a', '__class__', '__dict__' ...]
```
위와같이 `_클래스__변수`의 형태로 맹글링이 되었다. 여기서 __t 를 재정의 하고자 하면,
```python
#example 02
class Test:
    def __init__(self):
        self.__a = 1

t = Test()
t.__a
# AttributeError:
```
AttributeError가 발생한다. 그렇기 때문에 **해당 클래스를 상속하는 하위 클래스에서 재정의 되는 것을 막을 수 있다**.

### 4. `__double_leading_and_trailing_underscore__` : 파이썬에서 특수 용도로 사용한다. 특별한 메서드를 나타낸다 ex) `__init__`,`__str__` ...

---
## 3. I18n / L10n 함수로 쓸때
```python
import gettext

_ = gettext.gettext

print(_('This is a translatable string.'))
```
위와 같이 `gettext` 라이브러리를 이용해 컨벤션으로써 쓰인다.
