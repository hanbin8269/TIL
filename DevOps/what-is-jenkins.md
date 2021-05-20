# 젠킨스란?

## 기본 개념
- Java Runtime 위에서 동작하는 자동화 서버
    -> Jenkins가 돌아갈려면 **Java가 깔려 있어야 함**
- **빌드, 테스트, 배포 등 모든 것을 자동화** 해주는 자동화 서버
- **다양한 플러그인**들을 활용해서 각종 자동화 작업을 처리할 수 있음
- 일련의 자동화 작업의 순서들의 집합인 **pipeline을 통해 CI/CD 파이프라인을 구축**함


### Plugin?
젠킨스에는 여러 기능을 하나로 모듈화 시킨 플러그인이 여러개 존재한다. 대표적인 플러그인으로는 
- **`Credentials plugin`**
    배포에 필요한 **각종 중요 정보 (AWS token, Git access token, secret key, etc.)** 를 저장해 주는 플러그인
    알아서 암호화를 시켜주기 때문에 보안에도 좋은 성능을 보인다.
    또한, 젠킨스는 실행 할 때 private 한 공간에서 실행되기 때문에 보안에 강하다.
- **`Docker plugin`**
    젠킨스 내부에서 **docker build** 하고 **도커 허브로부터 pull** 받기 위해 사용되는 플러그인
- **`pipeline`**
    CI/CD 파이프라인을 젠킨스에 구현하기 위한 일련의 플러그인들의 집합이자 구성
    자세한 내용은 아래에서 설명
처음에 Recommend 해주는 것만 깔면 어지간한건 다 깔수 있다.

### Pipeline?

여러 플러그인들을 **이 파이프라인에서 용도에 맞게 사용하고 정의함**으로써 파이프라인을 통해 서비스가 배포된다.

두가지 형태의 **Pipeline Syntax(Declarative, Scripted Pipeline)** 이 있는데, 가독성이 높은 문법을 가진 **Declarative Pipeline Syntax**가 많이 사용된다.

#### Pipeline Syntax
##### Sesctions
- Agent section
    여러 젠킨스에게 일을 지정할 수 있는 섹션
    젠킨스 노드 관리에서 새로 노드를 띄우거나 혹은 docker 이미지를 통해서 처리할 수 있음
- Post section
    스테이지가 끝난 이후의 결과에 따라서 후속 조치를 취할 수 있다.
    ex) Success, failure, always, cleanup 등
    콘솔 하나 찍는다던가 슬랙에 메세지를 보낸다 던가의 작업이 가능
- Stages section
    어떤 일들을 처리할 것인지 일련의 stage를 정의한다.
    ex) build, deploy 등
- Steps section
    한 스테이지 안에서 단계로 일련의 스텝을 보여준다.

Jenkins pipeline 플러그인은 위와 같은 단계로 이루어져 있다.
##### Declareative
각 스테이지 안에서 어떤 일들을 할 것인지 정의하는 것이다.
Environment, stage, option, parameters, trigger, when 등의 Declarative가 있다.

- Environment : 어떤 pipeline이나 stage scope의 환경 변수를 설정한다.
- Parameter : 파이프라인 실행 시 파라미터를 받는다.
- Tigger : 어떤 형태로 트리거 되는가 (ex) 깃 소스코드를 3분에 한번씩 긁어 온다. 
- When : 언제 실행되는가