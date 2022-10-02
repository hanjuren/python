# 정규표현식
"""
정규 표현식(Regular Expressions)은 복잡한 문자열을 처리할 때 사용하는 기법으로
파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다. 정규 표현식을 배우는 것은 파이썬을 배우는 것과는 또 다른 영역의 과제이다.
"""
import re

# Dot .
# 모든 문자에 매치된다.
print(re.match('a.b', "abc"))  # a 와 b사이에 어떤 문자든 존재해야한다. None

# 반복 (*)
# * 기호는 반복을 의미하며 있을수도 없을수도 있는 경우를 의미한다.
print(re.match('ca*t', 'cat'))  # <re.Match object; span=(0, 3), match='cat'>
print(re.match('ca*t', 'cdt'))  # None

# 반복 (+)
# + 기호를 사용한 반복은 1개이상의 반복이 필수로 존재해야한다.
print(re.match('ca+t', 'cat'))  # <re.Match object; span=(0, 3), match='cat'>
print(re.match('ca+t', 'ct'))  # None

# 반복 ({m,n}, ?)
# {} 를 사요하면 반복 횟수를 고정할 수 있다.
print(re.match('ca{1,2}t', 'caat'))  # <re.Match object; span=(0, 4), match='caat'>
print(re.match('ca{1,2}t', 'caaat'))  # None

# ?
# ? 기호는 존재하거나 없을수 있을때 사용하는 기호이다.
print(re.match('ab?c', 'ac'))  # b가 없지만 매칭된다. <re.Match object; span=(0, 2), match='ac'>
print(re.match('ab?c', 'abc'))  # <re.Match object; span=(0, 3), match='abc'>

# re 모듈
# 파이썬은 정규 표현식을 지원하기 위해 re(regular expression의 약어) 모듈을 제공한다.
# re 모듈은 파이썬을 설치할 때 자동으로 설치되는 기본 라이브러리로 사용 방법은 다음과 같다.

# match 메서드 => 문자열의 처음부터 정규식과 매치되는지 조사한다.
p = re.compile('[a-z]+')
print(p.match("python"))  # <re.Match object; span=(0, 6), match='python'>
print(p.match("3 python"))  # 처음 글자가 3으로 조건에 부합하지 않느다. None

# search 메서드 => match 와 다르게 문자열 전체를 조회한다.
print(p.search("python"))  # <re.Match object; span=(0, 6), match='python'>
print(p.search("3 python"))  # <re.Match object; span=(2, 8), match='python'>

# findall 메서드 => 문자열의 단어를 정규식과 매칭하여 리스트형식으로 반환한다.
print(p.findall("Life is too short"))  # ['ife', 'is', 'too', 'short'] L은 대문자이기 때문에 제외됨

# finditer 메서드 =>  findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.
match_list = p.finditer("Life is too short")
for word in match_list:
    print(word)
# <re.Match object; span=(1, 4), match='ife'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>


# match 객체의 메서드
# group 메서드 => 매치된 문자열을 돌려준다.
print(p.match("python").group())  # python

# start 메서드 => 매치된 문자열의 시작 위치를 돌려준다. match는 언제나 0이다. 이유는 문자열의 시작부터 조회하기 때문
print(p.match("python").start())  # 0

# end 메서드 => 매치된 문자열의 끝 위치를 돌려준다.
print(p.match("python").end())  # 6

# span 메서드 => 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
print(p.match("python").span())  # (0, 6)

# 컴파일 옵션

# DOTALL, S 옵션 => \n 문자도 포함하여 매치된다.
r = re.compile('a.b', re.DOTALL)  # . 기호는 \n은 매치되지 않지만 DOTALL 옵션을 사용하면 \n까지 매치된다.
print(r.match('a\nb'))  # <re.Match object; span=(0, 3), match='a\nb'>

# IGNORECASE, I => 대소문자 구분없이 매치된다.
r2 = re.compile('[a-z]+', re.IGNORECASE)
print(r2.match('Python'))  # <re.Match object; span=(0, 6), match='Python'>

# MULTILINE, M => 여러줄의 문자열을 조회할때 사용한다.
data = """python one
life is too short
python two
you need python
python three"""

r3 = re.compile("^python\s\w+", re.M)
print(r3.findall(data))  # ['python one', 'python two', 'python three']

# VERBOSE, X => 정규식을 주석 또는 줄 단위로 구분하는 옵션이다.
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref2 = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)


# 기타 메타문자

# | 기호 => OR을 의미
r4 = re.compile('Red|Blue')
print(r4.match('Blue'))  # <re.Match object; span=(0, 4), match='Blue'>

# ^ 기호 => 문자열의 시작
r5 = re.compile('^Life')
print(r5.search('Life is too short'))  # <re.Match object; span=(0, 4), match='Life'>
print(r5.search('My Life is too short'))  # None

# $ 기호 => 문자열의 맨끝
r6 = re.compile('short$')
print(r6.search('Life is too short'))  # <re.Match object; span=(12, 17), match='short'>
print(r6.search('LIfe is too short, hello world'))  # None

# \A, \Z => 문자열의 시작과 끝을의미 ^, $와 같은의미지만 MULTILINE 옵션을 사용할 경우에 사용한다.
data1 = """Life is too short
hello world
python world
hello python
hello ruby
"""
r7 = re.compile("\ALife", re.M)
print(r7.findall(data1))  # ['Life']

print(re.search(r'word\Z', 'Line one word\nLine two\n', flags=re.M))

