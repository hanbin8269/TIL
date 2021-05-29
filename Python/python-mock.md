# Mock?
실제로 시스템은 하나의 모듈과 여러개의 모둘이 **잘 연계되어서 함께** 작동한다. 
하지만 테스트할 경우에 DB인스턴스와 같은 **의존성**들을 다 준비해서 테스트하기가 쉽지 않다. 

그렇기 때문에 여러 모듈의 **인터페이스**만 만들어 테스트하는 방법을 **`Mock`**이라 한다.

의존성이 있는 것들을 실제로 **실행시키지 않고** 
- 그 함수를 **잘 호출 했는가**
- 호출 했을 때 **적절한 인자**를 넘겼는가

만 확인한다.

## 동작 방식

```python
from app.models.users import User


class UserController:

    def get_user_by_id(self, user_id: int) -> User:
        user_instance = User.filter(user_id).first()
        return user_instance
```
위 `UserController.get_user_by_id` 메서드를 테스트 해보려고 하는데,
`User.filter` 함수는 DB와 연결이 되어 있어야 실행이 가능한 함수이다.
그럼 이 함수를 **`mocking`**시켜서 테스트 코드를 작성해 보자

```python
from unittest.mock import patch, Mock
from unittest import TestCase
from app.controllers.users import UserController


class UserControllerTest(TestCase):
    @patch("app.models.users.User.filter")
    def test_get_user_by_id(self, mock_user_filter):
        mock_user_filter.return_value.first.return_value = Mock(id=1)
        user_instance = UserController().get_user_by_id(1)
        self.assertEqual(user_instance.id, 1)  # user_instance.id의 값 비교
        mock_user_filter.assert_called_with(1)  # User.filter가 인자값으로 1을 받았는지 확인
```
위와 같이 `unittest.mock`의 `patch` 데코레이터를 이용해서 `User.filter`함수를 `mocking` 시켰다.

이러면 의존성이 있는 것들을 실제로 **실행시키지 않고** 
- 그 함수를 **잘 호출 했는가**
- 호출 했을 때 **적절한 인자**를 넘겼는가
를 테스트할 수 있다.

## MagicMock vs Mock
```python
from unittest.mock import Mock, MagicMock

mock = Mock()

print(len(mock))
# TypeError: object of type 'Mock' has no len()

magic_mock = MagicMock()

print(len(magic_mock))
# 0
```
Mock()은 해당 오브젝트의 매직메서드(`__str__`, `__len__`) 까지 Mocking 시켜주지 않는다. 반면 `MagicMock`의 경우는 아래와 같이 구현해 둔다.
```python
__lt__: NotImplemented
__gt__: NotImplemented
__le__: NotImplemented
__ge__: NotImplemented
__int__: 1
__contains__: False
__len__: 0
__iter__: iter([])
__exit__: False
__complex__: 1j
__float__: 1.0
__bool__: True
__index__: 1
__hash__: default hash for the mock
__str__: default str for the mock
__sizeof__: default sizeof for the mock
```