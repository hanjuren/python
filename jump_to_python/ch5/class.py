# 클래스

"""
다양한 언어에서의 클래스와 개념은 동일하다. 클래스는 커다란 추상화된 구조체이고
이를통해 생성하는 결과물을 객체라고 부른다.

간단한 계산기 클래스를 생성해보자.
"""


class FourCal:
    def __init__(self, num1, num2):
        self.num2 = num1
        self.num1 = num2

    def set_data(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def sub(self):
        return self.num1 - self.num2

    def div(self):
        return self.num1 / self.num2


sample = FourCal(0, 0)
print(type(sample))  # type 함수는 객체의 타입을 출력해준다.

a = FourCal(1, 1)
a.set_data(4, 2)
print(a.add())  # 6
print(a.mul())  # 8
print(a.sub())  # 2
print(a.div())  # 2


b = FourCal(3, 3)
print(b.add())  # 6
print(b.mul())  # 9
print(b.sub())  # 0
print(b.div())  # 1


# 상속
class MoreFourCal(FourCal):
    def pow(self):
        return self.num1 ** self.num2


c = MoreFourCal(2, 4)
print(c.pow())  # 16


# 메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2


d = SafeFourCal(4, 0)
print(d.div())  # 0
