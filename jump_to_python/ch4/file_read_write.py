# 파일 읽고 쓰기
import os

path = "./files"
os.makedirs(path, exist_ok=True)


file = open(f"{path}/new_file.txt", 'w')

# 파일 열기 모드
# r => 읽기 모드
# w => 쓰기 모드
# a => 추가 모드 (파일의 마지막에 내용 추가)

for i in range(1, 11):
    text = f"{i}번째 줄입니다.\n"
    file.write(text)

file.close()

file2 = open(f"{path}/read.txt", "r")
lines = file2.readlines()

for line in lines:
    print(line.strip())  # 줄바꿈 문자 제거

file2.close()

# 파일전체 읽기
file3 = open(f"{path}/read.txt", "r")
data = file3.read()
print(data)

file3.close()

# with문과 함께 사용하기
with open(f"{path}/read.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

