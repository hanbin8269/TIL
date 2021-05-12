# AWS 솔루션 아키텍트 문제 정리



#### Q. Q. 웹 애플리케이션에 XSS 공격을 막으러면 어떻게 해야 하는가?
-> Application Load Balancer에 WAF를 활성화 시킨다.

#### Q. Amazon RDS MySQL 다중 AZ DB 인스턴스를 사용하고 있습니다. 이 인스턴스를 내부 시스템이 데이터를 가져올 때 상당히 느랴집니다. 웹 사이트의 성능을 향상시키는 솔루션은 무엇입니까?
-> RDS DB 인스턴스에 읽기 전용 복제본을 추가하고 읽기 전용 복제본을 쿼리하도록 내부 시스템을 구성합니다.

#### Q. 회사에서 정적 웹 사이트를 온 프레미스로 호스팅하고 웹 사이트를 AWS로 마이그레이션하려고 합니다. 웹사이트는 빨리 로드되어야 합니다. 이 회사는 가장 비용 효율적인 솔루션을 원합니다.
-> 웹사이트 컨텐츠를 S3 버킷에 복사 하고 S3 버킷을 오리진으로 사용하여 Amazon Cloud Front를 구성합니다.

#### Q. 솔루션 아키텍트가 Amazon Linux 기반으로 하는 고성능 컴퓨팅(HPC) 환경을 위한 스토리지를 설계하고 있습니다. 워크로드는 공유 스토리지와 무거운 컴퓨팅이 필요한 많은 양의 엔지니어링 도면을 저장하고 처리합니다. 어떤 스토리지 옵션이 최선일까요?
-> Lustre for FSx
HPC가 들어가면 일단 FSx를 하라고 한다. 공부가 더 필요할듯

#### Q. 회사는 Amazon S3 버킷 내에서 정적 웹사이트를 호스팅 합니다. 솔루션 아키텍트는 실수로 삭제한 경우 데이터를 복구할 수 있는지 확인해야 합니다.
-> Amazon S3 버전 관리를 활성화 한다.
만약 버전 관리를 켜보고 데이터를 지우면 데이터의 Type에 "Delete marker"라는 표시가 되고 파일은 살아 있게 된다. 그리고 "Delete marker"를 지우면 파일이 복구된다.

#### Q. 한 프로덕션 애플리케이션에서 실시간 트랜잭션 처리를 하고자 한다. 이 회사는 동일한 데이터에 엑세스 하는 새로운 보고 도구를 출시하고 있습니다. 어떤 보고 도구가 최선입니까?
-> 다중 AZ 읽기 전용 복제본을 생성합니다

#### Q. 모든 팀의 AWS 계정에서 특정 서비스 또는 작업에 대한 엑세스를 제한하는 보안 팀. 모든 계정은 AWS Organizaion 의 대규모 조직에 속합니다. 솔루션은 확장 가능해야 하며 권한을 유지할 수 있는 단일 지점이 있어야 합니다. 이를 위해 솔루션 아키텍트는 무엇을 해야 합니까?
-> 루트 조직 단위에서 서비스 또는 작업에 대한 엑세스를 제한하는 service control policy를 만듭니다.



#### Q. 솔루션 아키텍트가 예정된 뮤지컬 이벤트를 위해 웹 사이트를 최적화 하고 있습니다. 공연 영상은 실시간으로 스트리밍되며 요청 시 제공됩니다. 이 행사는 전 세계 온라인 청중을 유치할 것으로 예상됩니다. 실시간 주문형 스트리밍의 성능을 향상시키는 서비스는 무엇입니까?
-> CloudFront
RTMP 딜리버리 메소드를 사용한다.

#### Q. ALB 뒤에 EC2 인스턴스에서 실행 될 웹 애플리케이션을 설계하고 있습니다. 애플리케이션의 악의적인 인터넷 활동 및 공격에 대해 복원력이 있고 새로운 일반적인 취약성과 노출로부터 보호할 것을 엄격히 여구합니다. 솔루션 아키텍트는 무엇을 권장해야 합니까?
-> AWS WAF에 적절한 관리형 규칙을 배포하고 ALB와 연결합니다.

만약 DDOS공격같은게 있으면 Shield가 맞음

---

**🤔CloudTrail의 데이터 이벤트 vs 관리 이벤트**
데이터 이벤트는 S3에 어떤 파일이 올라왔을때, 관리 이벤트는 EC2인스턴스 생성 또는 S3 버킷 생성과 같은 이벤트를 감지한다.

**🤔FIFO queue vs Standard queue**
FIFO queue는 하나의 큐만을 사용해서 순서가 지켜지는 반변, Standard queue는 여러개의 큐를 사용해 순서가 섞일 수도 있다.

**🤔service control policy?**
Master account에 여러 계정이 속해있다. Master 계정이 A라는 계정에게 초대장을 보내면 Master 계정은 A 계정을 관리 **ex) 서비스 제한** 할 수 있게 되고 A의 비용을 대신 부담하게 된다. 서비스 제한에 대한 정책을 만들어 여러 계정에 부여할 수 있는데 이것이 service control policy다.