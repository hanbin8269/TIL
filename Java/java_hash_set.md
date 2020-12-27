# HashSet이란?
`HashSet`은 `Set`인터페이스를 구현한 클래스다. `Set` 인터페이스는 객체를 중복해서 저장할 수 없으며, 순서가 존재하지 않는다. 

## 중복검사 하는 과정
객체를 저장하기 전에 `Object` 클래스의 `hashCode()` 메소드를 호출해서 해시 코드를 얻어낸 다음 저장되어 있는 객체들의 해시코드를 비교한다. 해시코드가 일치하는 객체가 있다면 `equals()` 메서드로 두 객체를 비교해 `true`가 반환된다면 동일한 객체로 판단하고 저장을 하지 않는다.

위와 같이 `hashCode()`메서드와 `equals()` 메서드로 중복을 판단하기 때문에 적절히 오버라이딩을 해줘야 한다

ex)
```java
@Override
public int hashCode(){
    return userId;
}
@Override
public boolean equals(Object obj){
    if (obj instanceof User){
        User user = (User)obj;
        return (userId == user.userId);
    }
}
```