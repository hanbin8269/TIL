# Set 인터페이스란

## HashSet이란?
`HashSet`은 `Set`인터페이스를 구현한 클래스다. `Set` 인터페이스는 객체를 중복해서 저장할 수 없으며, 순서가 존재하지 않는다. 

## 기본적인 사용법
```java
Set<String> set = new HashSet<String>();
// String으로 타입을 지정한 HashSet 변수 선언

set.add("hello");
set.add("bye");
set.add("bye");
// HashSet에 요소 추가 ("bye" 중복 추가)

Iterator ir = set.iterator();
// Iterator 생성

while(ir.hasNext()){ // 만약 다음 요소가 존재하면
    String str = ir.next(); // 꺼내
    System.out.println(str);
}
// hello
// bye (중복 추가 처리됨)
```

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

## TreeSet이란?
중복을 허용하지 않으면서 객체를 정렬하는 클래스다.

객체를 정렬하기 위해서는 정렬 기준을 정해줘야 하는데, 이를 위해서 구현해야 하는 인터페이스 중에서 `Comparable` 인터페이스와 `Comparator` 인터페이스가 있다.

### Comparable
`compareTo()`메서드를 구현해야 한다.
```java
@Override
public int compareTo(T obj){ // 제네릭 타입의 인스턴스를 매개변수로 갖는다.
    return Integer.compare(this.Id, obj.Id); // 기본 타입의 `compare()` 메서드를 써주는게 좋다고 한다. 
}

``` 

### Comparator
`compare()` 메서드를 구현해야 한다.
```java
@Override
public int compare(T obj1, T obj2){ // 
    return Integer.compare(obj1.Id, obj2.Id); // 오름차순 정렬
//  return Integer.compare(obj2.Id, obj1,Id); // 내림차순 정렬
}
```

### 두 방식의 차이점
보통 `Comparable` 인터페이스는 **일반적인 정렬**을 할 때 사용된다. 여기서 말하는 **일반적인 정렬**이란 오름차순, 내림차순과 같은 정렬을 말한다.

`Comparator` 인터페이스는 **특정한 정렬**을 할 때 사용된다. 예를 들어서 `Student`클래스를 구현한다고 치자, 이미 학번으로 정렬하는`compareTo()`메서드를 구현해놨는데, 갑자기 점수로 정렬하고 싶어졌다. 하지만 이를 위해서는 `compareTo()`를 수정해야 하는데 런타임 도중에 수정하는 것은 불가능 하다. 이때 다른 정렬 방식을 정의하기 위해서 `Comparator`인터페이스를 쓰는 것이다.
```java
Comparator<Student> scoreComparator = new Comparator<Student>() {
    @Override
    public int compare(Student student1, Student student2){
        return Integer.compare(student1.getScore(), student2.getScore());
    }
}

Collection.sort(studentList, scoreComparator);
```

이렇게 쓸 수도 있다.
```java
class MyComparator implements Comparator<String>{
    @Override
    public int compare(String s1, String s2){
        return s1.compareTo(s2) * -1;
    }
}

TreeSet<String> treeSet = new TreeSet<String>(new MyComparator());
```