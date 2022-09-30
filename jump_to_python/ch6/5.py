# 하위 디렉토리 검색
"""
특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야 할까?
"""
import os


def search(path):
    file_list = os.listdir(path)
    for file_name in file_list:
        full_name = os.path.join(path, file_name)

        if os.path.isdir(full_name):
            search(full_name)
        else:
            if os.path.splitext(file_name)[-1] == '.py':
                full_name = os.path.join(path, file_name)
                print(full_name)


search("/Users/hanjuryeon/study/python/jump_to_python")

print(list(os.walk("/Users/hanjuryeon/study/python/jump_to_python")))

all_list = list(os.walk("/Users/hanjuryeon/study/python/jump_to_python"))
for (path, dirs, files) in all_list:
    for file in files:
        ext = os.path.splitext(file)[-1]
        if ext == '.py':
            print(f"{path}/{file}")

