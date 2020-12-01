# 자바 상속

## 상속?

### 클래스에서 상속의 의미
- 새로운 클래스를 정의 할 때 이미 구현된 클래스를 상속(inheritance) 받아서 속성이나 기능이 확장되는 클래스를 구현함
- 자바에서는 다중상속 지원 X
- `하위 클래스가 상위 클래스를 상속받는다` 라고 생각하자

### 상속을 사용하는 경우
- 상위 클래스는 하위 클래스보다 일반적인 개념과 기능을 가징
- 하위 클래스는 상위 클래스보다 구체적인 개념과 기능을 가짐
```java
class Animal{

}

class Dog extends Animal{ // 개는 동물보다 구체적인 개념이다.

}
```

### 상속 특징
- `private`, 기본 접근 제한자를 쓰면 하위 클래스에서 접근 할 수 없음

=> `protected`를 쓰면 하위 클래스에서 접근 가능

### 상속받은 하위 클래스가 생성되는 과정
1. 하위 클래스가 생성 될 떄 상위 클래스가 먼저 생성 됨
```java
public class VIPCustomer extends Customer { // VIPCustomer가 Customer를 상속받았다. 
	double salesRatio;
	private int agentID;
	
	public VIPCustomer() {
		
		// super(); 컴파일 단계에서 이 코드가 기본적으로 들가게 됨
		customerGrade = "VIP";
		bonusRatio = 0.05;
		salesRatio = 0.1;
	}
}	
```
2. 상위 클래스의 생성자가 호출되고 하위 클래스의 생성자가 호출 됨 

    => 하위 클래스의 생성자에서는 무조건 상위클래스의 생성자가 호출되어야 함

만약, 상위 클래스의 기본 생성자가 없는 경우 (매개 변수가 있는 생성자만 존재하는 경우) 하위 클래스는 명시적으로 상위 클래스의 생성자를 호출해야 함

#### 업 캐스팅
**업캐스팅?**

상위 클래스 형으로 변수를 선언하고 하위 클래스 인스턴스를 생성 할 수 있음

하위 클래스는 상위 클래스의 타입을 내포하고 있으므로 상위 클래스로 묵시적 형변환이 가능 함

상속관계에서 모든 하위 클래스는 상위 클래스로 묵시적 형 변환이 됨 **하지만, 그 역은 성립하지 않음**
```java
Customer customerKim = new VIPCustomer(10020, "김유신");
// 상위 클래스               하위 클래스
```
하지만 `customerKim`는 `Customer`의 멤버변수, 메서드만 사용할 수 있다.

### 오버라이딩
상위 클래스에 정의된 메서드의 구현 내용이 하위 클래스에서 구현할 내용과 맞지 않는 경우 하위 클래스에서 동일한 이름의 메서드를 재정의 할 수 있음
```java
Customer vc = new VIPCustomer();
vc.calcPrice(10000);
```
여기서 `calcPrice(int)` 메서드는 `Customer`에서 선언된 메서드이며, `VIPCustomer`에서 오버라이딩 한 메서드이다. 그러면 `calcPrice(int)` 메서드는 어느 클래스의 메서드로써 호출 될까?

자바에서는 항상 인스턴스 (`VIPCustomer`)의 메서드가 호출된다. 여기서 오버라이딩 한 `calcPrice(int)`를 가상함수라 한다.

## 다형성?
- 하나의 코드가 여러 자료형으로 구현되어 실행되는 것
- 같은 코드에서 여러 실행 결과가 나옴
- 정보은닉, 상속과 더불어 객체 지향 프로그래밍의 가장 큰 특징중 하나
- 객체지향 프로그래밍의 유연성, 재활용성, 유지보수성에 기본이 되는 특징

```java
package polymorphism;

class Animal{
	
	public void move() {
		System.out.println("동물이 움직입니다");
	}
}

class Human extends Animal{
	
	public void move() {
		System.out.println("사람이 두발로 걷습니다");
	}
}

class Tiger extends Animal{
	
	public void move() {
		System.out.println("호랑이가 네 발로 뜁니다.");
	}
}

class Eagle extends Animal{
	
	public void move() {
		System.out.println("독수리가 하늘을 날아갑니다.");
	}
}

public class AnimalTest {

	public static void main(String[] args) {
		
		Animal hAnimal = new Human();
		Animal tAnimal = new Tiger();
		Animal eAnimal = new Eagle();
		
		AnimalTest test = new AnimalTest();
		test.moveAnimal(hAnimal);
		test.moveAnimal(tAnimal);
		test.moveAnimal(eAnimal);
		
	}

    // 다른 자료형을 오버로딩 할 필요 없이 
    // 하나의 메서드로 모두 다른 기능이 구현됨
	public void moveAnimal(Animal animal) { 
		animal.move();
	}
	
}
```
코드는 `moveAnimal` 로 **하나**지만 모두 다른 기능이 구현되었다.

#### 다형성의 이점
- 다양한 여러 클래스를 하나의 자료형(상위 클래스)으로 선언하거나 형변환 하여 각 클래스가 동일한 메서드를 오버라이딩 한 경우, **하나의 코드가 다양한 구현**을 실행 할 수 있음
- 유사한 클래스가 추가되는 경우 **유지보수에 용이하고** 각 자료형 마다 다른 메서드를 호출하지 않으므로 **코드에서 많은 if문이 사라짐**

### 다운 캐스팅
묵시적으로 상위 클래스 형변환된 인스턴스가 원래 자료형(하위 클래스)으로 변환되어야 할 때 다운 캐스팅이라 함

하위 클래스로의 형 변환은 명시적으로 되어야 한다
```java
Customer vc = new VIPCustomer(); // 업캐스팅은 묵시적으로 가능
VIPCustomer vCustomer = (VIPCustomer)vc; // 다운 캐스팅은 명시적으로!
```
여기서 `VIPCustomer vCustomer = (VIPCustomer)vc` 구문은 자료형만 같으면 에러를 뱉지 않는다. 하지만 아래의 상황의 경우 에러를 뱉는다.

```java
class Animal{
	
	public void move() {
		System.out.println("동물이 움직입니다");
	}
}

class Human extends Animal{
	
	public void move() {
		System.out.println("사람이 두발로 걷습니다");
	}

    public void readBooks() {
		System.out.println("사랑이 책을 읽습니다.");
	}
}

class Tiger extends Animal{
	
	public void move() {
		System.out.println("호랑이가 네 발로 뜁니다.");
	}

    public void hunting() {
		System.out.println("호랑이가 사냥을 합니다.");
	}
}
// 위와 같은 상위클래스 1개, 하위 클래스 2개의 관계가 주어졌을떄,


Animal hAnimal = new human();
Animal tAnimal = new Tiger();

Tiger tiger = (Tiger)hAnimal; // 여기서는 에러를 뱉지 않는다.

tiger.hunting(); // 컴파일 단계에서 에러가 발생한다...

//Exception in thread "main" java.lang.ClassCastException: class polymorphism.Human 
//cannot be cast to class polymorphism.Tiger (polymorphism.Human and polymorphism.
//Tiger are in unnamed module of loader 'app')
```
`Human` 인스턴스를 `Tiger` 타입으로 캐스팅 할 수 없다고 한다. 이런 상황을 방지하기 위해 `instanceof`를 사용한다.

```java
Animal animal = new Human();

if ( animal instanceof Tiger) { // animal이 tiger의 객체인가?
	Tiger tiger = (Tiger)animal;
	tiger.hunting();
}
```
위와 같이 `instanceof`를 사용하면 에러를 방지할 수 있다.