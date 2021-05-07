# Python Functools


## lru_cache
함수의 반환값을 메모리제이션하는 데코레이터

arguments에 따른 return값이 1대 1일 때 사용한다. (입력값에 따른 출력값이 하나일때)

```python
@lru_cache(maxsize=128)
def get_hasher(algorithm: str = "default"):
    if algorithm == "default":
        return BcryptSHA256PasswordHasher()

    raise ValueError("Not found algorithm")
```
와 같이 사용한다.
### Python 3.7 vs 3.8
[링크](https://hanbin8269.tistory.com/22)를 참고하자