# XSS (Cross Site Scripting)

## XSS가 뭐지?
사용자 입력 값에 대한 필터링이 제대로 이루어지지 않은 경우에, 악의적인 사용자가 공격하려는 사이트에 스크립트를 넣는 기법을 말한다.
사이트에 접속한 사용자가 스크립트를 실행하게 된다면 보통 쿠키나 세션의 민감한 정보를 탈취하거나 의도치 않은 행동을 수행시킨다.

-------------
## XSS 종류
#### 1. Stored XSS
공격자가 커뮤니티나 댓글에 악성코드를 작성해놓고, 희장자가 로드할때 실행되는 방법이다.

ex) 댓글에 악성코드를 게시해놓으면, 

#### 2. Reflected XSS
공격자가  dHTTP 요청에 악성 콘텐츠를 주입하면 그 결과가 사용자에게 **반사되는** 형태이다.

ex) 링크를 클릭하도록 피해자를 유도하고, 세션을 가로챌 수 있다.

----------
## 발생할 수 있는 피해
1. 쿠키 정보/세션 ID 가로채기
2. 시스템 관리자 권한 획득
3. 공격자가 원하는 웹페이지로 리다이렉션
--------
## 예방 방법
#### 입출력 값 검증 및 무효화
   
   스크립트 등 해킹에 사용될 수 있는 코딩에 사용되는 입력 및 출력 값에 대해서 **검증하고 무효화** 시켜야 한다. 
   
   ex) XSS 공격에서는 기본적으로 `<script>`를 사용하기 떄문에 태그문자(`<, >`) 등 위험한 문자를 입력 했을때 **필터링**을 해준다.

#### OWASP ESAPI 라이브러리
> `※ OWASP : The Open Application Security Project`
> 
>`※ ESAPI : The OWASP Enterprise Security API`

`ESAPI`에는 총 14개의 API가 있는데, 이 중 XSS의 취약점을 예방하기 위해 만들어진 API는 `validator`와 `encoder`가 있다. `validator`는 입력값을 필터링, `encoder`는 출력값을 인코딩 및 디코딩 하는 기능을 가지고 있다.

----------

## 예시
내가 자주 사용하는 `Django` 프레임 워크에서는 기본적으로 `HTML escape`라는 기능이 켜져있다. 장고 템플릿에서는 `{% autoescape on %}`를 작성하면 처리가 된다.

DRF에서는  `Serializer`에서 `django.utils.html`의 `escape()` 메소드를 사용해 처리할 수 있다
```python
from django.utils.html import escape

class MySerializer:
    def validate_myfield(self, value):
        return escape(value)
```