# 함수

"""

"""


# 함수의 구조
def function_name(args):
    print(args)


# 매개변수와 인수
# 매개변수란 함수로 전달된 값을 받는 변수를 의미
# 인수란 함수를 호출할때 전달하는 입력값을 의미한다.
def add(a, b):  # a, b 는 매개변수
    return a + b


print(add(1, 2))  # 인자


# 입력값과 결과값에 따른 함수의 형태

# 1. 일반적인 함수
# 입력값과 결과값이 있는 함수
def function1(a):
    return a * 2


# 2. 입력값이 없는 함수
def function2():
    return "Hello Python"


result = function2()
print(result)


# 3. 결과값이 없는 함수
def function3(a):
    print(a)


function3(1)


# 입력값의 갯수가 명확하지 않을때
def function4(*args):
    number = 0
    for num in args:
        number += num

    return number


value = function4(1, 2, 3)
print(value)


# 매개변수에 초기값 설정하기
def say_myself(name, age, man=True):
    gender = "남자" if man else "여자"

    return f"이름: {name}, 나이: {age}, 성별: {gender}"


v = say_myself("한주련", 26)
print(v)

# 함수 내부에서 외부의 변수값을 변경하는 방법
a = 1
b = 1


# return 사용하기
def vartest1(a):  # return 사용하기
    a += 1
    return a


a = vartest1(a)
print(a)


# global 사용하기
def vartest2():  # global 키워드는 사용하지 않는것이 좋다. 외부변수에 종속적인 함수는 좋은 함수가 아니다.
    global b
    b += 1


vartest2()
print(b)


# lambda
# lambda는 함수를 생성할때 사용하는 예약어로 def키워드와 동일한 역할을 한다.
# 아래 def 키워드를 통해 생성한 함수와 lambda로 생성한 함수는 동일한 결과를 만들어낸다.
def add1(a, b):
    return a + b


add2 = lambda a, b: a + b


print(add1(1, 2))
print(add2(1, 2))  # lambda 함수는 return 명령어가 없어도 결과값을 돌려준다.
