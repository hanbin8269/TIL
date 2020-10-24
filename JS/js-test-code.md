# Koa.js Testcode 작성하기

동아리 프로젝트를 진핸하면서, Koa.js 를 이용해 서버를 개발하게 되었다.
백엔드 팀장이 TDD사용을 권하면서 Testcode 작성법을 알려줬다.

```javascript
import * as request from 'supertest';
```
를 작성해서 `supertest`라이브러리를 선언해 준다.

```javascript
describe('login', ()=>{  // login 테스트 묶음을 만든다.
    it('should be failed with incorrect user info', aync() =>{
    // 올바르지 않은 유저 정보라면 실패해야 한다.
        const response = await request(app.callback())
        .post('/api/user/v1/login')
        .send({
          email: 'hanbin8269@gmail.com',
          password: '0128gksqls',
        });
    
    expect(response.status).toBe(200);
    // response.status 가 200이면 테스트 통과!
  });
})
```
그리고 `describe`로 테스트 묶음을 만들고 `it('', aync()=>{})` 메서드의 콜백함수를 이용해 테스트를 만든다.
그리고 `expect` - `toBe`를 이용해 기대되는 값이 나온다면 테스트를 통과시킨다.