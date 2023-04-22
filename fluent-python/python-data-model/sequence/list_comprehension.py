arr = []
for num in range(1, 11):
    arr.append(num)
print(arr)

arr = [num for num in range(1, 11)]
print(arr)

# 두가지 색상과 세가지 크기의 티셔츠 리스트 만들기
colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']
tshirt1 = []
for size in sizes:
    for color in colors:
        tshirt1.append((size, color))
print(tshirt1)

tshirt2 = [(size, color) for size in sizes for color in colors]
print(tshirt2)


