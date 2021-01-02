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
- 정적 내부 클래스
- 지역 내부 클래스
- 익명 내부 클래스

