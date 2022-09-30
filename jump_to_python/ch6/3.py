# 메모장 만들기
"""
원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
"""

# 메모 추가
import sys
option = sys.argv[1]

if option == '-a':
    with open("memo.txt", 'a') as f:
        data = sys.argv[2]
        f.write(f"{data}\n")
elif option == '-v':
    with open("memo.txt") as f:
        memo = f.read()
        print(memo.strip())


