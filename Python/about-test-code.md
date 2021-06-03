# 테스트 코드에 대해

## 단위 테스트 vs 기능 테스트

### 단위 테스트 (Unit Test)
- 개발자 뷰에서 보는 테스트 `ex) 아이디와 패스워드를 넣고 그것을 검증하는 "함수"에 대한 테스트`
- 함수단위로 테스트한다
- 단위를 isolation(격리) 시키기 위해서 mock을 사용한다.
- 상대적으로 빠르다.

### 기능 테스트 (Function Test)
- 사용자 뷰에서 보는 테스트 `ex) 실제로 로그인을 브라우저에서 해보는 테스트`
- 요구사항(기능)을 단위로 테스트한다.
- 상태를 만들어 놓기 위해 fixture를 사용 `ex) 로그인 테스트를 위해 유저를 생성해 놓음`
- 다양한 것들이 통합적으로 테스트 되기 때문에 상대적으로 느리다.


## unittest
- 파이썬 표준 라이브러리
- 테스트 자동화
- 테스트 구조화
- 테스트 결과 보고

등의 역할을 수행하는 라이브러리다.
### unittest.TestCase
독립적인 테스트 단위

### 기본적인 사용
```python
import unittest


class HelloTest(unittest.TestCase):
    def test_success(self):
        self.assertEqual(0,0)

    def test_failure(self):
        self.assertEqual(0,1)
        
if __name__ == '__main__':
    unittest.main()
```

```
$ python .\test2.py
F.  ※ 다른 테스트에 영향을 주지 않는다.
======================================================================
FAIL: test_failure (__main__.HelloTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\test2.py", line 9, in test_failure  ※ 어느 부분에서 실패 했는지 알려준다.
    self.assertEqual(0,1)
AssertionError: 0 != 1

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

테스트를 작성 하다보면 실패한 테스트만 다시 돌리고 싶을 때가 있다.

그럴때는
```
$ python .\test2.py HelloTest.test_failure
```
와 같이 인자값으로 테스트를 적어 넣어주면 된다

또, 하위 디렉토리의 모든 테스트를 실행하고 싶을 때가 있다.

그럴때는
```
$ python -m unittest discover 
```
를 입력하면 하위 디렉토리의 모든 테스트를 실행한다. (기본적으로 "test*.py" 포맷의 파일을 찾아 실행한다.)

## 의존성이 있는 테스트의 경우
```python
def get_username(user_id):
    user = db.user.query(user_id = user_id)
    return user.name
```
위와 같은 코드는 DB가 있어야 테스트가 가능하다. 또한, 테스트 전에 데이터를 넣어주어야 한다. 

이럴때는 **Mock** 이라는 것을 사용한다.

```python
exist_user = User.filter(User.email == email).first()
```
위와 같이 `filter` 메서드의 결과값을 `first` 메서드로 처리하는 함수는 아래와 같이 처리 할 수 있다.
```python
from unittest import patch


class TestUserController(TestCase):
    @patch("app.models.users.MentoringField.filter")
    def test_update_user_successful(
        self, mock_mentoring_field_filter
    ):
        credentials = {
            "mentoring_fields": ["backend"],
            "name": "hanbin",
            "self_introduction": "heelo, im hanbin",
            "phone_number": "01082693188",
            "profile_image": "s3.13224",
        }

        mock_mentoring_field_filter.first().return_value = "backend"  # 여기!
        try:
            user_instance = UserController().update_user(1, **credentials)
        except HTTPException as exe:
            self.fail(exe.detail)
```