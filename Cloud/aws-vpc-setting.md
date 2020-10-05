# AWS VPC 설정 방법

## vpc란
> 참고 (https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/what-is-amazon-vpc.html)

VPC 핵심 개념
- **Virtual Private Cloud(VPC)** — 사용자의 AWS 계정 전용 가상 네트워크
- **서브넷** — VPC의 ip 주소 범위
- **라우팅 테이블** — 네트워크 요청이 향할 위치를 제어
- **가용 영역** — 각 리전에 개별 데이터 센터 (각자 물리적으로 격리 되어있음)
- **인터넷 게이트웨이** — VPC에서 인터넷으로 아웃바운드 통신을 가능케 해줌
![screenshot_20171221-151714](https://miro.medium.com/max/1000/1*C_j93s0KB4JwfLgck5YFug.png)