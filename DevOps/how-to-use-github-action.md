# Github Action 사용법

## Github Action 이란?
- Github 저장소를 기반으로 소프트웨어 개발 workflow를 자동화 할 수 있도록 도와주는 도구 
- ex) Test Code 실행, 자동 배포
  
**※ workflow? 일의 흐름 또는 비즈니스 프로세스**

## push할 때 Test Code 실행하기
프로젝트 root 디렉토리에 `.github\workflows\<파일 이름>.yml` 파일을 만든다.
![how-to-use-github-action-01](../images/how-to-use-github-action-01.png)