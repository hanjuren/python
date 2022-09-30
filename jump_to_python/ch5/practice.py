# 1
# 다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
#
# print(cal.value) # 10에서 7을 뺀 3을 출력


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


# 2.
# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.

# cal = MaxLimitCalculator()
# cal.add(50) # 50 더하기
# cal.add(60) # 60 더하기
#
# print(cal.value) # 100 출력
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)  # 50 더하기
cal.add(60)  # 60 더하기
print(cal.value)  # 100 출력


# 3.다음 결과를 예측해 보자.

# 하나.
# >>> all([1, 2, abs(-3)-3])
# False
# 둘.
# >>> chr(ord('a')) == 'a'
# True


# 4. filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
arr = [1, -2, 3, -5, 8, -3]
new_arr = list(filter(lambda num: num > 0, arr))
print(new_arr)


# 5.
# 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
#
# >>> hex(234)
# '0xea'
# 이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
print(int(0xea))


# 6.
# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
arr = list(map(lambda num: num * 3, [1, 2, 3, 4]))
print(arr)


# 7.
# 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
# [-8, 2, 7, 5, -3, 5, 0, 1]
arr = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(arr))
print(min(arr))


# 8.
# 17 / 3의 결과는 다음과 같다.
# >>> 17 / 3
# 5.666666666666667
# 위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.
print(round(17 / 3, 4))


# 9.
# 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:\doit\myargv.py)를 작성해 보자.
#
# C:\> cd doit
# C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
# 55
#
# .myargv.py
# import sys
#
# total = 0
# for i in range(1, len(sys.argv)):
#     total += int(sys.argv[i])
# print(total)


# 10.
# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
# C:\doit 디렉터리로 이동한다.
# dir 명령을 실행하고 그 결과를 변수에 담는다.
# dir 명령의 결과를 출력한다.
import os
os.chdir("./package")
f = os.popen("ls")
print(f.read())


# 11.
# glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
import glob
f = glob.glob("./package/*.py")
print(f)


# 12.
# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32
import time
print(time.strftime('%Y/%m/%d %X', time.localtime(time.time())))


# 13.
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨).
import random

lotto_arr = []
while len(lotto_arr) < 6:
    random_number = random.randint(1, 45)

    if random_number not in lotto_arr:
        lotto_arr.append(random_number)
    else:
        print(f"{random_number}은 중복 번호 입니다.")

print(lotto_arr)




