# 1
# import package.sub1.echo
#
# package.sub1.echo.echo_test()

# 2
# from package.sub1 import echo
#
# echo.echo_test()

# 3
# from package.sub1.echo import echo_test
# echo_test()

# 주의
# 도트 연산자를 사용하여 imoprt 할때 마지막 항목은 반드시 모듈 또는 패키지여야 한다.
# import package.sub1.echo.echo_test
# Traceback (most recent call last):
#   File "/Users/hanjuryeon/study/python/jump_to_python/ch5/package_test.py", line 17, in <module>
#     import package.sub1.echo.echo_test
# ModuleNotFoundError: No module named 'package.sub1.echo.echo_test'; 'package.sub1.echo' is not a package

# __init__.py 의 용도
# __init__.py 는 해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다.
# 3.3 이후 버전부터는 __init__.py가 없어도 패키지로 인식하지만 하위버전 호환성을 위해 작성하는 방식도 나쁘지 않다.



