# 객체지향 프로그래밍 SOLID 원칙

클린코드로 유명한 로버트 마틴이 좋은 객체 지향 설계의 5가지 원칙을 정리한 것이다.

## SRP 단일 책임 원칙
Single Responsibility Principle
- 한 클래스는 하나의 책임만 가져야 한다.
- 하나의 책임이라는 것은 모호하다
    - 클 수 있고, 작을 수 있다.
    - 문맥과 상황에 따라 다르다.
- **중요한 기준은 변경이다** 변경이 있을 때 파급 효과가 적으면 단일 책임 원칙을 잘 따른 것.
- ex) UI 변경, 객체의 생성과 사용을 분리

## OCP 개방-패쇄 원칙
Open/Closed Principle
- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.
- 다형성을 활용하자
- 인터페이스를 구현한 새로운 클래스를 하나 만들어서 새로운 기능을 구현
### 문제점
```java
public class MemberService {
    private MemberRepository memberRepository = new MemoryMemberRepository();
}
////

public class MemberService {
    // private MemberRepository memberRepository = new MemoryMemberRepository();
    private MemberRepository memberRepository = new JdbcMemberRepository();
}
```
위 코드를 보면 `OCP`를 지키기 위해 인터페이스(`memberRepository`)를 만들고 클래스(`JdbcMemberRepository`)를 구현 해 `MemberService`에 선언한 모습이다. 하지만 `MemberService`가 **변경**되었다. 즉, 클라이언트 코드가 변경되었기 때문에 `OCP`를 원칙을 지킬 수 없게 된다.

이 문제점을 해결하기 위해서 객체를 생성하고, 연관 관계를 맺어주는 별도의 **조립, 설정자**가 필요하다.  

## LSP 리스코프 치환 원칙
Liskov Substitution Principle
- 프로그램의 객체는 **프로그램의 정확성**을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.
- 다형성에서 하위 클래스가 **인터페이스의 규약**을 다 지켜야 한다는 원칙이다. 인터페이스를 구현한 객체를 믿고 사용하려면, 이 원칙이 필요하다.
- 단순히 컴파일만 성공하는 것이 아닌 **규약**을 지켜야 한다.
- ex) 자동차 인터페이스에서 엑셀을 **앞으로 가라**는 기능인데, **뒤로 가도록** 구현하면 `LSP` 위반이다.

## ISP 인터페이스 분리 원칙
Interface Segregation Principle
- **특정 클라이언트를 위한** 인터페이스 **여러 개가** 범용 인터페이스 하나보다 낫다
- 자동차 인터페이스 -> 운전 인터페이스, 정비 인터페이스로 분리
- 사용자 클라이언트 -> 운전자 클라이언트, 정비사 클라이언트로 분리
- 분리하면 정비 인터페이스 자체가 변해도 운전자 클라이언트에 **영향을 주지 않음**
- 인터페이스가 **명확**해지고, **대체 가능성이 높아진다**.

## DIP 의존관계 역전 원칙
Dependency Inversion Principle
- 프로그래머는 추상화에 의존해야지, 구체화에 의존하면 안된다.
- 구현 클래스에 의존하지 말고, **인터페이스에 의존**하라는 뜻이다.
- 역할과 구현을 철저히 분리하자

```java
public class MemberService {
    private MemberRepository memberRepository = new MemoryMemberRepository();
}
```
위 코드를 보면 구현 클래스에 의존하고 있다. 그렇기 때문에 `DIP`에 위반된다.

----------
SOLID 5원칙을 잘 살펴보았다. 객체 지향의 핵심을 다형성 이라고 알고 있었는데, 위에서 언급한 문제들을 보면 다형성 만으로는 `OCP`, `DIP`를 지킬 수 없다는 것을 알게되었다. 무언가 더 방법이 없을까?

스프링에서는 이를 해결하기 위해 `DI(Dependency Injection)`이라는 기술을 사용한다.