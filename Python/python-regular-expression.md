# 파이썬 정규 표현식
정규표현식은 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어이다

## 메타문자
```
. ^ $ * + ? { } [ ] \ | ( )
```
위와 같은 문자들을 **메타문자** 라고 한다.

이중에 문자클래스라고 불리는 `[ ]`에 대해 먼저 알아 볼 것이다.
## 문자 클래스
`[ ]` 안에 들어간 정규식은 **[ ]사이의 문자들과 매치** 라는 의미를 갖는다.

만약 정규 표현식이 `[abc]` 라면 **a,b,c 중 한 개의 문자와 매치** 라는 의미를 가진다. 자주 사용하는 [ ]문자 클래스 몇가지를 알아보자

`[a-zA-Z]` : 알파벳 전부
`[0-9]` : 숫자만
`[^0-9]` : 숫자가 아닌 문자만
**※ 앞에 `^`가 들어가면 그 반대라는 의미를 가진다** 

```python
import re

p = re.compile('[a-z]')
print(p.findall('Hello :)'))
# ['e', 'l', 'l', 'o']
```

## 문자 집합

```python
p = re.compile('\w')

print(p.match('aaa'))
# <re.Match object; span=(0, 1), match='a'>

p = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
print(p.search('저의 전화번호는 010-1234-5678 입니다'))
# <re.Match object; span=(9, 22), match='010-1234-5678'>
```
`\d` : `[0-9]` 
`\D` : `[^0-9]`
`\w` : `[a-zA-Z0-9]`
`\W` : `[^a-zA-Z0-9]`
`\s` : `[\t\n\r\f\v]` (공백)
`\S` : `[^\t\n\r\f\v]`
`\b` : `\bhello\b` hello 앞뒤가 공백일때
`\B` : `\Bhello\B` hello 앞뒤가 공백이 아닐때

## . 모든 문자
```python
p = re.compile('l.l')

print(p.findall('loool'))
# []
print(p.findall('l&l'))
# ['l&l']
```
`a.b`는 a와 b사이에 하나의 어떤 문자가 들어오든 매칭된다. 단, 개행문자(`\n`)는 제외한다

## * 반복
```python
p = re.compile('l*')

print(p.findall('loool'))
# ['l', '', '', '', 'l', '']
print(p.findall('l&l'))
# ['l', '', 'l', '']
print(p.findall('asd'))
# ['', '', '', '']
```
\* 앞에 있는 문자가 **몇개가 오든 (0개도 포함)** 모두 매치된다

## + 한 번 이상 반복
```python
p = re.compile('l+ ')

print(p.findall('loool'))
# ['l', 'l']
print(p.findall('l&l'))
# ['l', 'l']
print(p.findall('asd'))
# []
```
\+ 앞에 있는 문자가 **최소 한번 이상 반복** 되어야 매치된다

## ? 없거나 하나만 있거나
```python
p = re.compile('ba?d')

print(p.findall('bd'))
# ['bd']
print(p.findall('bad'))
# ['bad']
print(p.findall('baaaaaaad'))
# []
```
\? 앞에 있는 문자가 **없거나 하나만 있거나**일때 매치된다. 두개 이상은 안된다
