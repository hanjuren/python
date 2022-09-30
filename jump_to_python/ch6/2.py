# 게시판 페이징
"""
A 씨는 게시판 프로그램을 작성하고 있다.
그런데 게시물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.
"""


def get_total_page(total, limit):
    if total % limit == 0:
        return total // limit
    else:
        return (total // limit) + 1


print(get_total_page(11, 5))
