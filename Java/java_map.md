# java map 인터페이스란?

## HashMap 클래스
Map 인터페이스를 구현한 클래스 중 가장 일반적으로 사용하는 클래스이다

### 사용법
- **선언**
```java
HashMap<Inteher, String> hashMap = new HashMap<Integer, String>();
// key의 타입은 Integer, value의 타입은 String으로 선언했다.
```

- **정보 넣기**
```java
hashMap.put(1,"정한빈");
// 1이라는 key에 "정한빈" 이라는 value를 가진 객체를 집어넣었다.
```

- **정보 삭제**
```java
hashMap.remove(id);
// id라는 key를 가지고 있는 객체를 제거했다.

if (hashMap.containsKey(id)){
    hashMap.remove(id)
}
// id라는 key를 가진 객체가 있을때 제거
```

- **정보 조회**
```java
hashMap.get(id)
// id라는 key를 가지고 있는 객체 조회

Iterator<Integer> ir = hashMap.keySet().iterator();
// hashMap의 key가 Set 타입으로 반환된다
while(ir.hasNext()){
    int key = ir.next();
    
    System.out.println(hashMap.get(key));
}
// hashMap 모두 조회
```
## TreeMap 클래스
key 객체를 정렬하여 key-value를 pair로 관리하는 클래스

key로 사용되는 클래스에 Comparable, Comparator 인터페이스를 구현해야 한다.

사용방법은 위에서 소개한 `hashMap`과 비슷하다.