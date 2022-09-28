# 문자형
# 문자열은 값을 바꿀수 업는immutable한 자료형이다.

# 파이썬에서 문자열 자료형을 만드는 방법은 총 4가지로 구성

# 1
str1 = "파이썬 프로그래밍"

# 2
str2 = '파이썬 프로그래밍'

# 3
str3 = """파이썬 프로그래밍"""

# 4
str4 = '''파이썬 프로그래밍'''


# 문자열 내부에 작은 따옴표
str5 = "'안녕하세요'"
print(str5)  # '안녕하세요'

# 문자열 내부에 큰따옴표
str6 = '"안녕하세요"'
print(str6)  # "안녕하세요"

# \ 를 이용하여 내부에 따옴표 넣기
str7 = "\"안녕하세요\""
print(str7)

# 변수에 여러줄인 문자열 대입

# \n 사용
str8 = "안녕하세요\n반갑습니다."
print(str8)

# """ 또는 '''
str9 = """
안녕하세요
반갑습니다.
"""
print(str9)

# 파이썬에서는 문자열을 이용한 연산이 가능하다.
name = "한주련"
print("안녕하세요 제 이름은 " + name + "입니다.")

print("=" * 20)
print("hello world")
print("=" * 20)

# 문자열 길이 구하기
str10 = "hello python"
print(len(str10))

# 문자열 indexing, slicint
a = "Life is too short, You need Python"
print(a[3])  # e
print(a[-1])  # n

print(a[0:4])

# 포맷팅
# 숮자 대입
print("저는 %d살 입니다." % 26)

# 문자열 대입
print("제이름은 %s 입니다." % "한주련")

# 문자열 관련 함수

s = "Hello python"
# 찾고자 하는 문자열 갯수 반환
print(s.count('o'))

# 찾는 문자열의 첫번떄 인덱스 반환
# 만약 값이 존재하지 않는다면 -1 반환
print(s.find('e'))

# find 메서드와 비슷하나 값이 존재하지 않으면 에러가 발생
# print(s.index('a'))
"""
Traceback (most recent call last):
  File "/Users/hanjuryeon/study/python/jump_to_python/ch2/strint_type.py", line 81, in <module>
    print(s.index('a'))
ValueError: substring not found
"""
print(s.index('o'))

# 문자열 삽입
print(','.join(s))  # H,e,l,l,o, ,p,y,t,h,o,n

# 대문자, 소문자 변환
print(s.upper())
print(s.lower())

# 문자열 바꾸기
print(s.replace("Hello", "Hi"))

# 문자열 나누기
print(s.split())
