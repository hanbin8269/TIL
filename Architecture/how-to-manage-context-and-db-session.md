# How to manage context and db session

애플리케이션 컨텍스트와 DB 세션을 관리하는 방법을 설명 할 것이다

## 애플리케이션 컨텍스트 관리
설명하기 앞서 애플리케이션 컨텍스트란 무엇인지 알아보자.

애플리케이션 컨텍스트는 리퀘스트 컨텍스트와 비교하여 설명할 수 있는데,

#### 목적
- 애플리케이션 컨텍스트는 **현재 활성화된 애플리케이션**을 위한 인스턴스이고 ex) FastAPI app
- 리퀘스트 컨텍스트는 **현재 Request**를 위한 인스턴스 이다. ex) http 요청 객체(body, header, cookie 등의 content를 가지는)
#### 담고있는 정보
- 애플리케이션 컨텍스트는 애플리케이션을 위한 정보를 담고있다. ex) DB 엔진 정보, secret key와 같은 세팅 정보 등
- request 컨텍스트는 현재 Request 에 대한 정보를 담고있다. ex) 요청 path, header, cookie 등

