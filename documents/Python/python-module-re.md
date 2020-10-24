# python `re` 모듈
## re.match
```python
import re

print(re.match('a','aaa'))
# <re.Match object; span=(0, 1), match='a'>
print(re.match('a','abc').span())
# (0, 1)
# 0번째 문자부터 1번째 문자 까지 매치한다
print(re.match('a','baa'))
# None
```
`re.match`메서드는 **문자열의 처음부터** 시작하여 패턴이 일치하는지 확인한다.

## re.search
```python
import re

print(re.search('a','aba'))
# <re.Match object; span=(0, 1), match='a'>
print(re.search('a','bbb'))
# None
print(re.search('aa','baa'))
# <re.Match object; span=(1, 3), match='aa'>
#       1번째 문자부터 3번째 문자까지 매칭됨
```
`re.search` 메서드는 `re.match`와는 다르게 **중간부터 라도** 패턴이 일치하는지 확인한다.

## re.findall
```python
import re

print(re.findall('a','asdasda'))
# ['a', 'a', 'a']
print(re.findall('a','bbb'))
# []
print(re.findall('aaa','aaaa'))
# ['aaa']
```
다른 함수와 다르게 `list`형식으로 반환한다

## re.finditer
```python
import re

match_iter = re.finditer('a','aaab')

print(match_iter)
# <callable_iterator object at 0x00000200C8F04470>
# iterable 객체 반환
for i in match_iter:
    print(i)
# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='a '>
```
`re.finditer`는 Iterable 객체를 반환하여 `for in` 문에서 활용할 수 있다.

## re.fullmatch
```python
import re

print(re.fullmatch('a','a'))
# <re.Match object; span=(0, 1), match='a'>
print(re.fullmatch('a','aaa'))
# None
print(re.fullmatch('a','bbb'))
# None
```
패턴과 문자열이 완벽하게 일치하는지 검사한다. 남는 부분이 있어도 `None`을 반환한다

## match object 메서드
```python
import re

obj = re.search('he','hello!')

print(obj.group()) # 일치한 문자열 반환
# "he"
print(obj.start()) # 일치한 문자열의 시작 위치 반환
# 0
print(obj.end()) # 일치한 문자열의 끝 위치 반환
# 2
print(obj.span()) # 일치한 문자열의 시작 끝 튜플로 반환
# (0, 2)
```

-----
`re` 모듈은 정규표현식을 표현하거나 필터링할때 자주 사용된다.