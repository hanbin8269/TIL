# java 내부 클래스
## 내부 클래스란?
- 클래스 내부에 구현한 클래스
- 클래스 내부에서 사용하기 위해 선언하고 구현하는 클래스다.
- 주로 외부 클래스 생성자에서 내부 클래스를 생성한다.

```java
class OutClass{
    private int num;
    private InClass inClass;
    
    public OutClass(){
        inClass = new InClass(); // 생성자에서 인스턴스 생성
    }
    
    class InClass{ // 내부 클래스
        private String name;
    }
}
```

## 내부 클래스의 유형
- 인스턴스 내부 클래스
```java
class OutClass{
    class InClass{
    }
}
```
- 정적 내부 클래스
```java
class OutClass{
    static class InClass{
    }
}
```
- 지역 내부 클래스

```java
class OutClass {

    Runnable getRunnable(int i) {
        
        class MyRunnable implements Runnable{
            @Override
            public void run(){
                System.out.println("runnable");
            }
        }
        
        return new MyRunnable();
    }
}
```
- 익명 내부 클래스
```java
class OutClass {
    Runnable runner = new Runnable() {
        @Override
        public void run() {
            System.out.println("runnable");
        }
    };
}
```

## 람다식
- 자바에서 함수형 프로그래밍을 구현하는 방식
- 클래스를 생성하지 않고 함수의 호출만으로 기능을 수행

### 함수형 프로그래밍이란?
- 순수 함수를 구현하고 호출한다.
- 입력받은 자료를 기반으로 수행되고 외부에 영향을 미치지 않으므로 병렬처리등에 사용 가능하다.
- 안정적이며 확장성 있는 프로그래밍 방식이다.

**※ 순수함수 : 외부 변수를 사용하지 않고 매개 변수만 사용해서 구현하는 함수**

### 문법
```java
(x,y) -> {System.out.println(x + y);}
```
기본적인 문법
```java
str -> {System.out.println(str);}
```
매개변수 하나일 경우 괄호 생략 가능
```java
str -> System.out.println(str);
// str -> return str.length(); // return 문은 중괄호 생략 불가능 
```
중괄호 안의 구현부가 하나일 경우 중괄호 생략 가능
```java
(x,y) -> x+y
str -> str.length()
```
중괄호 안의 구현부가 반환부 하나라면 `return`과 중괄호 모두 생략 가능