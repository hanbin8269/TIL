# Python Functools


## lru_cache
함수의 반환값을 메모리제이션하는 데코레이터

arguments에 따른 return값이 1대 1일 때 사용한다. (입력값에 따른 출력값이 하나일때)

```python
import functools

@functools.lru_cache(maxsize=128)
def get_hasher(algorithm: str = "default"):
    if algorithm == "default":
        return BcryptSHA256PasswordHasher()

    raise ValueError("Not found algorithm")
```
와 같이 사용한다.
### Python 3.7 vs 3.8
[링크](https://hanbin8269.tistory.com/22)를 참고하자

## partial
하나 이상의 argument가 이미 채워진 함수의 새 버전을 만들기 위해 사용된다.
```python
import functools

def print_hello(repeat):
    print("hello " * repeat)


three_hello = functools.partial(print_hello, repeat=3)

three_hello()
# hello hello hello
```
위와 같이 repeat argument의 기본값을 3으로 고정한 함수를 만들 수 있다.