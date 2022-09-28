# 1. 주어진 자연수가 홀수인지 짝수인지 판별하는 is_odd 함수 만들기
def is_odd(num):
    return "짝수입니다." if num % 2 == 0 else "홀수입니다."


result1 = is_odd(70)
result2 = is_odd(71)
print(result1)
print(result2)


# 2. 입력으로 들어오는 모든 수의 평균값을 계산하기 (들어오는 수의 개수는 정해져 있지 않음)
def avg_numbers(*args):
    total_num = 0
    for num in args:
        total_num += num

    return total_num / len(args)


result = avg_numbers(1, 2, 3, 4, 5)
print(result == 3)


# 3. 두개의 숫자를 입력받아 더하여 돌려주는 프로그램 수정
# 코드예시
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

# 수정
input3 = int(input("첫번째 숫자를 입력하세요:"))
input4 = int(input("두번째 숫자를 입력하세요:"))

total = input3 + input4
print("두 수의 합은 %s 입니다" % total)


# 4. 다음중 출력결과가 다른것
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# print("you", "need", "python") 콤마는 띄어쓰기가 된다.


# 5. test.txt 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f2 = open("test.txt", 'r')
# print(f2.read())
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

with open("test.txt", 'w') as file:
    file.write("Life is too short")

with open("test.txt", 'r') as file:
    print(file.read())


# 6. 사용자의 입력을 받아 test.txt에 저장하는 프로그램을 작성
# 단 다시 실행해도 기존 작성내용을 유지하고 새로입력한 내용을 추가
data = input()
with open("test.txt", "a") as file:
    file.write(f"\n{data}")


# 7. 다음과 같은 내용을 가진 파일이 있다. 이 파일의 내용중 java라는 문자열을 python으로 바꿔서 저장해보자
with open("test2.txt", "r") as file:
    lines = file.readlines()

with open("test2.txt", "w") as file:
    for line in lines:
        file.write(line.replace('java', 'python'))
