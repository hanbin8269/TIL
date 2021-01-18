# 객체 지향 프로그래밍 - 특징

## 다형성
다형성(polymorphism)이란 같은 자료형에 여러가지 객체를 대입하여 다양한 방법으로 동작하는 성질을 의미한다.

  ```java
    // ex)
  interface Animal{
    void run();
    void eat();
  }
  
  class Human implements Animal{
    @Override
    void run(){ 
        System.out.println("사람이 뛴다");
    }
  
    @Override
    void eat(){ 
        System.out.println("사람이 먹는다");
    }
  }
  
  class Tiger implements Animal{
    @Override
    void run(){ 
        System.out.println("호랑이가 뛴다");
    }
  
    @Override
    void eat(){ 
        System.out.println("호랑이가 먹는다");
    }
  }
```
위 예제를 보면서 이 문장을 나눠서 생각해보자.
- **같은 자료형에 여러가지 객체 대입** - 말 그대로 하나의 자료형이 여러가지의 타입을 가질 수 있는 것
  ```java
  public class AnimalTest{
    public static void main(String[] args){
        Animal h = new Human(); // Animal 이라는 하나의 자료형에 Human, Tiger 라는 여러가지 타입을 가지고 있다.
        Animal t = new Tiger();
    }
  }
  ```
- **다양한 방법으로 동작** - 오버로딩, 오버라이딩 등을 통해 메소드를 재정의 하는 것
  ```java
  public class AnimalTest{
    public static void main(String[] args){
        Animal h = new Human();
        Animal t = new Tiger();
        
        h.run(); // 사람이 뛴다
        t.run(); // 호랑이가 뛴다
  
        // 위와 같이 오버라이딩을 통해 메소드를 재정의 하고 다양한 방법으로 동작되고 있다.
    }
  }
  ```
이와 같은 다형성을 잘 지켰다면, 아래와 같은 효과를 볼 수 있다.
- 인터페이스를 구현한 객체 인스턴스를 실행 시점에 유연하게 변경할 수 있다.
- 클라이언트를 변경하지 않고, 서버의 구현 기능을 유연하게 변경할 수 있다.
