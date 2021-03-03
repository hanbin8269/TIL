# ASGI란?

ASGI는 Asynchronous Server Gateway Interface의 약자이며, 

웹 서버와 프레임워크, 어플리케이션을 비동기로 연결해주는 파이썬의 표준 인터페이스 이다.

## WSGI와 다른점
WSGI는 애플리케이션 코드에서 서버 코드를 분리할 수 있는 표준 인터페이스다.

WSGI는 파이썬 프레임워크 및 웹 서버에서 유연한 동작을 지원했으나, HTTP 형식 (request/response)에 고정되어 있다는 문제점이 있었다.

즉, WSGI는 동기 호출 방식이라는 점이 ASGI와 차이를 가진다.
