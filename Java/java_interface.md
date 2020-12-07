# 자바 인터페이스

## 인터페이스란?
추상 메서드로만 이루어진 클래스이며,

어떤 오브젝트에 대한 명제 라고 생각하면 된다.

## 인터페이스의 요소
- 추상 메서드 (구현 코드가 들어가지 않음)
- 상수
- 디폴트 메서드
- 정적 메서드
- private 메서드

## 인터페이스 선언 방법
```java
public interface Calc{
    double PI = 3.14; // 상수로 변환됨
    // public static final double PI = 3.14; 와 같음
    int add(int num1, int num2); // abstract를 안붙여도 추상메서드로 변환 됨

    
    public String stringAdd(String s1, String s2);
    // 어떤 매개변수를 받아서 어떤 타입으로 반환을 하는지 명시
}
```
위와 같이 인터페이스를 선언하고 아래와 같이 상속받는다.
```java
public class Calculator implements Calc{

    @Override
    public int add(int num1, int num2) {
    	return 0;
    }   

    @Override
    public int substract(int num1, int num2) {
    	return 0;
    }   

    @Override
    public int times(int num1, int num2) {
    	// TODO Auto-generated method stub
    	return 0;
    }   

    @Override
    public int divide(int num1, int num2) {
    	// TODO Auto-generated method stub
    	return 0;
    }   

    @Override
    public String stringAdd(String s1, String s2) {
    	// TODO Auto-generated method stub
    	return null;
    }
}
```
하나라도 구현하지 않은 기능이 있다면 에러가 발생하게 된다.