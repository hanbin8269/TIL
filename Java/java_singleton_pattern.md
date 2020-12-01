# 자바 싱글톤 패턴

## 싱글톤 패턴?
디자인 패턴의 일종으로, 전역 변수를 사용하지 않고 **객체를 하나만** 생성하도록 하며, 생성된 객체를 **어디에서든지 참조**할 수 있도록 하는 패턴 이다.

=> **하나의 인스턴스만**을 생성해야 하며, `getInstance` 메서드를 통해 **모든 클라이언트에게 동일한** 인스턴스를 반환하는 작업을 수행한다.
- 생성자는 `private`으로 `static`으로 유일한 객체 생성
- 외부에서 유일한 객체를 참조할 수 있는 public static get() 구현

```java
public class Company {
	
	private static Company instance = new Company(); // private과 static으로 유일한 객체 생성
	
	private Company() {} // private 생성자
	
	public static Company getInstance() { // 외부에서 유일하게 객체를 참조할 수 있는 방법
		
		if(instance == null) {
			instance = new Company();
		}
		return instance;
	}
}

```

```java

public class CompanyTest {

	public static void main(String[] args) {
		
		Company company1 = Company.getInstance(); // getInstance 로만 참조
		Company company2 = Company.getInstance();
		
		System.out.println(company1); // staticex.Company@73a8dfcc
		System.out.println(company2); // staticex.Company@73a8dfcc 동일한 메모리 주소 값을 가진다.
		
	}

}
```