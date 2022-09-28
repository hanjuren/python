# for문

"""
파이썬의 for문은 파이썬의 직관적인 특징을 가장 잘 대변해주는 문장의 특징을 가지고 있다.
"""

# 기본 구조
for a in [1, 2, 3, 4]:
    print(a)

marks = [
    {"name": "james", "mark": 90},
    {"name": "lisa", "mark": 40},
    {"name": "tom", "mark": 60},
]

for mark in marks:
    if mark['mark'] < 60:
        print(f"{mark['name']}학생은 불합격입니다.")
    else:
        print(f"{mark['name']}학생은 합격입니다.")


# 리스트 내포
a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num)

arr = [num for num in a]
print(result)
print(arr)