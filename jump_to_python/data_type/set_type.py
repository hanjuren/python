# set 자료형

"""
set 자료형은 중복을 허용하지 않는 특성과 순서가 없다는 특징이 있다.
이러한 이유로 set 자료형은 딕셔너리와 마찬가지로 인덱싱이 불가능 하다.
만약 set 자료형의 값을 인덱싱으로 접근하려면 리스트 변환 후 접근이 가능하다.
"""

set1 = {1, 2, 3, 1}
print(set1)

set2 = set("hello")
print(set2)

# 관련 함수

# 값 추가하기

# 1개일때
set1.add(4)
print(set1)

# 추가하려는 값이 2개 이상일때
set1.update([5, 6])
print(set1)

# 값 제거
set1.remove(5)
print(set1)
