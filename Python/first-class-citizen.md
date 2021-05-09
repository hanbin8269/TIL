## Python 1급 객체

OOP를 공부하다 보면 가끔 **1급 객체(first-class citizen)** 혹은 **1급 함수**에 대한 언급을 볼 수 있다.

이것에 대한 지식이 없을때 항상 **이 두가지**가 궁금했다.

1. **1급 객체**란 무엇일까?
2. 함께 언급 되는 **고차 함수**는 무엇일까?

두가지만 알아보자

그런데 설명하기 앞서, **1급 객체**와 **1급 함수**는 같은 개념이란 것을 알아두자

### 1. 1급 객체란 무엇일까?
1급 객체는 3가지 조건을 모두 충족하는 객체를 말한다.
```
1. 변수나 데이터에 할당 할 수 있어야 한다.
2. 객체의 인자로 넘길 수 있어야 한다.
3. 객체의 반환값으로 반환할 수 있어야 한다.
```
[위키피디아 링크](https://en.wikipedia.org/wiki/First-class_citizen#History)

간단히 말하자면, **Object로서의 특성을 모두 지닌 것**을 **1급 객체**라고 부른다.

**Python의 함수**는 위 세가지 조건을 모두 충족한다.
그렇기 때문에 **Python의 함수**는 일급 객체라고 할 수 있다.

참고로, **Python의 모든 것은 객체이다.**

예시를 보면서 이해해보자

```python
# 1. 변수나 데이터에 할당 할 수 있어야 한다.
def print_hello():
    print("hello!")

a = print_hello  # print_hello 함수를 a라는 변수에 저장
a()
# hello!
```
```python
# 2. 객체의 인자로 넘길 수 있어야 한다.
def introduce(name):
    return "hello, my name is" + name

def goodbye(name):
    return "bye bye, " + name


def who_i_am(func, name):
    return func(name)

who_i_am(introduce, "hanbin")
# hello, my name is hanbin
who_i_am(goodbye, "hanbin")
# bye bye, hanbin
```
```python
# 3. 객체의 반환값으로 반환할 수 있어야 한다.
def test_hasher(data):
    return "hashed" + data

def get_hasher():
    return test_hasher  # test_hasher함수를 반환한다.

hasher = get_hasher()
hashed_data = hasher("hanbin")
print(hashed_data)
# hashed hanbin
```

### 고차 함수(higher-order function)?
```
1. 객체의 인자로 넘길 수 있어야 한다.
2. 객체의 반환값으로 반환할 수 있어야 한다.
```
두가지 조건을 충족하는 함수를 말한다.