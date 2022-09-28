# while문

"""
조건이 참인 동안 실행되는 반복문
"""

hit = 1

while hit <= 10:
    print(f"나무를 {hit}번 찍었습니다.")

    if hit == 10:
        print(f"{hit}번 찍어 안남어가는 나무는 역시 없군요..")

    hit += 1


prompt = """
1. Add
2. Del
3. List
4. Quit
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())


coffee = 10
money = 300

while money:
    print("커피 나왔습니다.")
    coffee -= 1
    print(f"남은 커피 {coffee}잔")

    if coffee == 0:
        print("커피 품절")
        break

coffee = 5
while True:
    money = int(input("돈을 넣어주세요"))

    if money == 300:
        print("커피나왔습니다.")
        coffee -= 1
    elif money > 300:
        print(f"커피와 거스름돈 {money - 300}원 입니다.")
        coffee -= 1
    else:
        print("입력하신 금액으로는 커피를 살 수 없습니다.")

    if coffee == 0:
        print("커피 품절 영업종료")
        break

