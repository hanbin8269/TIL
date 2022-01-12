# How to manage context and db session

애플리케이션 컨텍스트와 DB 세션을 관리하는 방법을 설명하겠습니다

## 리퀘스트 컨텍스트란
요청중에 실행되는 각 함수에서 요청과 관련된 url, params, body, cookie 와 같은 값들을 하나하나 인자값으로 넘겨받기 쉽지 않습니다.
그렇기 때문에 요청이 진행되는 동안에 요청에 관련된 데이터를 담고있는 공간이 필요한데, 그 역할을 하는 것이
리퀘스트 컨텍스트입니다.

플라스크 같은 경우에는 요청이 시작 될 때 Request 객체를 글로벌하게 생성하고 스레드에 푸시하게 됩니다.

그리고 요청이 끝날 때 pop되어 처리됩니다.

stack 공간은 스레드 끼리 서로 공유하지 않기 때문에 각 스레드마다 별도의 Request 객체 (Request 컨텍스트)를 가지게 될 수 있습니다

아래와 같이 request (from flask import request) 객체는 _request_ctx_stack.top 의 request 객체와 동일합니다.
```python
# flask/globals.py

def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)

...
request: "Request" = LocalProxy(partial(_lookup_req_object, "request"))  # type: ignore
```

## 애플리케이션 컨텍스트
애플리케이션 컨텍스트는 리퀘스트 컨텍스트가 푸시 될 때 함께 푸시됩니다.

또한 리퀘스트 컨텍스트가 pop될 때 pop 처리됩니다.

아래와 같이 current_app 은 _app_ctx_stack.top 의 app과 동일합니다.
```python
# flask/globals.py L44

def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app


# context locals
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
current_app: "Flask" = LocalProxy(_find_app)  # type: ignore
```