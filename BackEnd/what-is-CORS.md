# What is CORS? (Cross Origin Resource Sharing)

서버를 개발하다보면 프레임워크에서 기본으로 제공하는 CORS 미들웨어에 의해 접근이 막힐때가 있다. CORS가 무엇일까?

## 의미
**Cross Origin Resource Sharing (CORS)** 은 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 HTTP Header를 사용하여 브라우저에 알려주는 체제이다.

만약 `https://hanbin.com`의 JavaScript코드가 `XMLHttpRequest`로 `https://hellllolo.com/data.json`을 요청하는 경우 CORS 에러가 발생한다. 

**※ XMLHttpRequest? 서버로부터 데이터를 요청하는 규격이며, Ajax에서 많이 사용한다.**

## 해결법
`Access-Control-Allow-Origin`등의 헤더를 추가해 `cross-origin`을 허락한다.

## 동작 방식
![출처 :  https://en.wikipedia.org/wiki/Cross-origin_resource_sharing](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcs4wto%2FbtqzZKoD3Mi%2FWcisEe9B1vsXyZCtzbO150%2Fimg.png)
>출처 : https://en.wikipedia.org/wiki/Cross-origin_resource_sharing``

1. `Access-Control-Request-Method`, `Access-Control-Request-Headers`헤더를 추가해 `OPTIONS` 메서드로 사전 요청을 보낸다
2. 서버에서  `Access-Control-Allow-Methods`헤더로 `POST`, `GET`, `OPTIONS` 메서드로 자원에 접근 가능 하다는 응답을 준다
3. OK이며 사용가능한 메서드라면, 요청하고자 하는 자원(API)를 요청한다
4. 서버에서 응답한다.