# 1

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# shirt

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

num = 1
result = 0
while num <= 1000:
    if (num % 3) == 0:
        result += num
    num += 1

print(result)

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
"""
*
**
***
****
*****
"""
n = 1

while n <= 5:
    print("*" * n)
    n += 1

# 4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1, 101):
    print(i)


# 5
"""
A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for문을 사용하여 A 학급의 평균 점수를 구해 보자.
"""
marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
for mark in marks:
    total += mark

result = total / len(marks)
print(result)


# 6
"""
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
        
위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
"""
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
