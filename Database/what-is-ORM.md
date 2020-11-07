# ORM(Object Relational Mapping)이란?
데이터베이스와 객체를 자동으로 매핑 해주는 것을 말한다.
## 왜 필요할까?
**객체 지향 프로그래밍**은 **클래스**를 사용하고 **데이터베이스**는 **테이블**을 사용한다.
이때 둘간의 **불일치(Impedance Mismatch)** 가 발생하게 된다. 
이때 ORM을 통해 객체 간의 관계를 바탕으로 SQL을 생성하여 **불일치**를 해결하는 방법이다.

## ORM 종류

#### Django의 Models, orm query
```python
# Models
from django.db import models

class User(models):
    email = models.CharField(unique=True)
    nickname = models.CharField()
    age = models.IntegerField()
```
위와 같이 `class` 객체를 작성하면 orm에 의해 db가 생성된다.
```python
# ORM Query
User.objects.filter(email='hanbin8269@gmail.com')
    .order_by('email')
    .values('email','nickname') # 원하는 칼럼만
```
`select`문은 위와 같이 사용한다.

#### Prisma 
`GraphQL`스키마를 기반으로 DB를 생성해준다. 아직 제대로 사용해 본적이 없지만 후에 사용할 의향이 있다.

## 객체 관계 불일치 (Impedance Mismatch)
위에서 말했듯이 기존 관계형 데이터베이스와 프로그래밍 언어 사이의 데이터 구조, 기능 등의 차이로 발생하는 충돌을 말한다.

객체 관계 불일치에는 여러 종류가 있다.
#### Granularity(세분성)
DB의 **테이블 갯수**보다 객체 지향 언어의 **클래스 객체 모델**이 더 많아 질 수 있다라는 의미를 가진다. 이를 **클래스 객체 모델**이 더 세분화 되었다고 말한다.

#### Inheritance(상속성)
**상속**은 객체 지향 언어만의 특징이다. 그렇기 때문에 RDB는 객체의 상속을 표현하는 개념이 없다

#### Identity(일치)
RDB는 **기본키**를 통해서 일치의 개념을 정확히 정의한다. 하지만 객체 지향 프로그래밍에서는 **주소값의 일치, 내용의 일치**의 경우를 구분하여 정의한다.

#### Association(연관성)
객체 지향 언어는 방향성이 있는 **객체 참조**를 사용하여 **연관성**을 나타내지만, RDB는 방향성이 없는 **외래키**로 **연관성**을 나타낸다.

#### Navigation(탐색)
객체 지향 언어는 객체의 관계를 이용해서 줄줄이 타고가며 탐색해 비효과적 이지만, RDB는 객체의 탐색을 시작하기 전에 쿼리의 수를 최소화 하고 JOIN을 통해 엔티티를 불러오고 해당하는 엔티티를 선택한다.