# Docker 컨테이너 만들기 및 사용법

## docker 설치하가
#### Docker for window를 설치하기
[Docker for window](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
여기서 `Get Docker`버튼을 눌러주자 글구 하라는대로 계속 해주자...
설치가 모두 완료되고 나면,

![what-is-docker-02](../images/what-is-docker-02.png)

위와 같이 작업 표시줄에서 우클릭을 하고 `Settings`에 들어가 주자

![what-is-docker-03](../images/what-is-docker-03.png)

그리고 `Expose daemon on tcp ...` 를 체크해주고 apply를 해주자.

이러면 이제 기본적인 세팅을 끝났다.

#### 왜 가상환경도 설치했을까?
도커는 기본적으로 `Linux`환경에서만 지원된다. `Windows` 환경에서는 `Hyper-V`를 설치하여 그 위에서 `Docker`가 돌아간다.


#### 오류가 났다...
```
Raw-mode is unavailable courtesy of Hyper-V. (VERR_SUPDRV_NO_RAW_MODE_HYPER_V_ROOT)
```
라는 에러메세지가 검출되었다... 구글링을 해보자 `Virtual Box`와 `Docker desktop`을 함께 써서 나타나는 오류라고 한다. 그래서 `Virtual Box`를 삭제해 주니 잘 돌아간다

## Docker 기본 명령어

#### `docker version`
`docker`의 버전을 확인한다. 
```python
C:\Users\user>docker version
Client: Docker Engine - Community
 Cloud integration: 1.0.2
 Version:           19.03.13
 API version:       1.40
 Go version:        go1.13.15
 Git commit:        4484c46d9d
 Built:             Wed Sep 16 17:00:27 2020
 OS/Arch:           windows/amd64 # Client는 Window 환경
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.13
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       4484c46d9d
  Built:            Wed Sep 16 17:07:04 2020
  OS/Arch:          linux/amd64 # Server는 Linux 환경에서 제공된다
  Experimental:     false
  ```

#### `docker run`
컨테이너를 실행하는 명령어 이다.
여러 옵션이 있는데 알아보자

- `-d` : `detached mode` 흔히 말하는 백그라운드 모드
- `-p` : 호스트와 컨테이너의 포트를 연결(포워딩)
- `-v` : 호스트와 컨테이너의 디렉토리를 연결 (마운트)
- `-e` : 컨테이너 내에 사용할 환경변수 설정0
- `--name` : 컨테이너 이름 설정
- `--rm` : 프로세스 종료 시 컨테이너 자동 제거
- `-it` : `-i`와 `-t`를 동시에 사용한 것으로 터미널 입력을 위한 옵션
- `--network` : 네트워크 연결

##### ex)
```
> docker run --rm -it ubuntu:16.04 /bin/sh

Unable to find image 'ubuntu:16.04' locally
16.04: Pulling from library/ubuntu
2c11b7cecaa5: Pull complete
04637fa56252: Pull complete
d6e6af23a0f3: Pull complete
b4a424de92ad: Pull complete
Digest: sha256:bb69f1a2\
Status: Downloaded newer image for ubuntu:16.04
#
```
위 명령어는 `ubuntu:16.04`이미지로 한 컨테이너를 실행하고, 배쉬 쉘을 실행 하라는 명령어 이다. 또한, `--rm` 옵션을 추가해서 프로세스 종료 시 컨테이너가 자동으로 제거되도록 했다.

##### 웹 애플리케이션을 실행시켜 보자
```python
docker run -d # 백그라운드로 실행
  -p 4568:4567 # 컨테이너 로컬 4568 포트와 호스트 4567 포트 연결
  -e ENDPOINT=https://workshop-docker-kr.herokuapp.com/ # 애플리케이션에서 사용할 환경변수 입력
  -e PARAM_NAME=hanbin # 위와 동일
  subicura/docker-workshop-app:2 # 이 이미지의 버전2 사용
```
위 명령어를 입력하면 실행한 컨테이너의 ID값이 나오며 성공한다.

##### Redis를 실행시켜 보자
`Redis`는 메모리 기반의 `"key" : Value` 구조 데이터 관리 시스템 이다.
```
docker run --name=redis -d -p 1234:6379 redis
```
`telnet`으로 테스트 해보면 제대로 작동하는 것을 알 수 있다.
```
docker run --rm -it mikesplain/telnet docker.for.win.localhost 1234

set hello world
get hello
$5
world
```

##### MySQL을 실행시켜 보자
[docker hub mysql](https://hub.docker.com/_/mysql) 에 접속해 보면 여러 설정을 알 수 있고 어떤 환경 변수를 사용할 수 있는지 알 수 있다.
```
docker run -d -p 3306:3306 \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=true \
  --name mysql \
  mysql:5.7
```
위 명령어로 `mysql` 컨테이너를 생성했다
```
> docker exec -it mysql mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.32 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```
위 명령어로 `mysql` 컨테이너에 접근해서 `mysql` 명령어를 실행시켰다.

## 네트워크를 만들어 보자
도커 컨테이너 끼리 통신을 할 수 있는 가상 네트워크를 만들 수 있다.
예를 들어 wordpress과 mysql이 서로 통신을 하려면 서로의 ip를 입력해야 한다. 

그렇게 된다면 mysql 접속한다면 host의 ip를 알고 있거나 도메인으로 관리 해야 한다. 
하지만 네트워크를 만들어 연결한다면, 컨테이너의 이름만으로 접속 할 수 있다.

아래의 예시를 보자
```python
docker network create app-network # app-network라는 이름의 네트워크 생성

docker run --name=ubuntu -d -it --network=app-network ubuntu:16.04 /bin/sh  # ubuntu 라는 이름의 데몬 컨테이너 생성
docker run --name=ubuntu2 -it --network=app-network ubuntu:16.04 /bin/sh  # ubuntu2 라는 이름의 컨테이너 생성
# docker network connect app-network ubuntu2 명령어로 이미 생성된 컨테이너를 추가할 수도 있다.
```
위와 같이 컨테이너를 연걸 할 수있다.

```python
docker run -d -p 8080:80 \
  --network=app-network \
  -e WORDPRESS_DB_HOST = mysql \ # mysql이라는 이름의 컨테이너를 호스트로 지정
  -e WORDPRESS_DB_NAME = wp \ # wp라는 이름의 컨테이너를 DB이름으로 지정
  wordpress
```
## docker-compose
`docker-compose`는 여러개의 컨테이너를 실행시키기고 정의하기 위한 툴이다. `YAML`파일을 사용하여 서비스를 구성한다.
아래 yml 파일을 보자
```yml
# docker-compose.yml

version: '2'
services: 
  db: # db라는 이름의 서비스
    image: mysql:5.7 # mysql:5.7 이미지
    volumes: # 호스트의 디렉토리를 컨테이너 디렉토리와 연결
      - ./mysql:/var/lib/mysql # 호스트의 ./mysql 디렉토리에 컨테이너의 /var/lib/mysql 디렉토리 마운트
    restart: always
    environment: # 환경 변수 설정
      MYSQL_ROOT_PASSWORD: wordpress
      MTSQL_DATABASE: wordpress
      MTSQL_USER: wordpress
      MTSQL_PASSWORD: wordpress
  wordpress:
    image: wordpress:latest
    volumes:
      - ./wp:/var/www/html
    ports: # 외부포트 : 내부포트
      - "8000:80"
    restart: always
    environment: 
      WORDPRESS_DB_HOST : db:3306
      WORDPRESS_DB_PASSWORD : wordpress
```
위 `yml` 파일을 작성하고 `docker-compose up` 명령어를 입력하면 컨테이너가 생성 및 실행되고, `docker-compose down` 명령어를 입력하면 생성된 컨테이너가 종료된다.

### 궁금한점
##### 파일명이 `docker-compose.yml`이 아니더라도 실행이 될까?
`docker-compose -f hello.yml up` 과 같이 `-f`옵션을 붙여 파일을 지정해 줄 수 있다.
