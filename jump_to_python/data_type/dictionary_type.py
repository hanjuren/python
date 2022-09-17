# 딕셔너리 자료형

# 딕셔너리 자료형은 Hash 구조로 key와 value가 쌍으로 이루어진 자료형을 의미한다.

dic = {'name': 'han', 'phone': '01011111111', 'birth': '1210'}
print(dic['name'])

# 관련 함수들

# key 목록
key_arr = dic.keys()
print(key_arr)

# keys 메서드는 dic_keys 객체를 리턴하는데 리스트형식의 반환값이 필요하다면 list 메서드를 통해 리스트를 생성이 가능하다.
key_list = list(dic.keys())
print(key_list)

# dic_keys, dic_items, dic_values 객체는 리스트 변환 없이도 반복문 사용이 가능하다.
for key in dic.keys():
    print(key)
