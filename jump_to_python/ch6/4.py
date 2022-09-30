# 탭을 공백 4개로 치환하기
"""
문서 파일을 읽어서 그 문서 파일 안에 있는 공백을 줄바꿈으로 바꾸어 주는 스크립트를 작성해 보자.
다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.
python tabto4.py 원본파일, 새파일이름
"""

import sys

with open(f"{sys.argv[1]}") as f:
    data = f.read().strip()
    new_data = data.replace(" ", "\n")

with open(f"{sys.argv[2]}", 'w') as f:
    f.write(new_data)



