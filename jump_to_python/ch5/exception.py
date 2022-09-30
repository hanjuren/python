# 에러 처리
# 기본적으로 try except를 사용하여 처리한다.
import logging

try:
    f = open("없는파일.txt", 'r')
except Exception as e:
    print(e)

# finally
try:
    4 / 0
except Exception as e:
    print(e)
finally:
    print("무조건 실행되는 코드")

# else
try:
    4 / 2
except Exception as e:
    print(f"오류 발생 {e}")
else:
    print("오류가 발생하지 않았습니다.")
finally:
    print("마지막")

# 오류 회피하기
try:
    4 / 0
except Exception as e:
    pass


# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()


# 예외 만들기
class Error(Exception):
    pass


def error_test(num):
    try:
        if num == 1:
            raise Error("에러 테스트")
        else:
            print(num)
    except Error as error:
        logging.error('Unexpected error: %s', error)


error_test(1)

