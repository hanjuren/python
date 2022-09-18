# if문

"""
if 작성시 조건에 해당하는 작업의 코드를 작성할때는 들여쓰기에 유의해야한다.
모든 들여쓰기는 같은 깊이에서 작성해야 코드가 정상적으로 실행된다.
"""

result = True

if result:
    print("True")
else:
    print("False")

# 조건문 작성 중 &&, || 연산자를 작성할때 파이썬에서는 and, or, not 으로 작성한다.

if 1 > 0 and 1 < 2:
    print("1은 0보다 크고 2보다는 작습니다.")

if 1 < 0 or 1 < 2:
    print("1은 0보다는 작지 않지만 2보다는 작습니다.")

if not 1 < 0:
    print("1이 0보다 작지 않다면 출력됩니다.")

# x in y, x not in y
# in, not in 조건문은 값이 리스트나 튜플 또는 문자열에 포하되는지 여부를 파악하는 조건문이다.

if 'a' in ['a', 'b', 'c']:
    print("리스트에 a 가 포함되어있습니다.")

if 'a' in ('a', 'b', 'c'):
    print("a 가 튜플에 포함되어있습니다.")

if 'a' not in "hello world":
    print("hello world에는 a 라는 문자열이 없습니다.")


# 조건문의 실행될 코드를 작성중 아무일도 일어나지 않게 하기위해서는 pass를 적용한다.

if True:
    pass


# 조건부 표현식
message = "success" if 60 < 70 else "fail"
print(message)
