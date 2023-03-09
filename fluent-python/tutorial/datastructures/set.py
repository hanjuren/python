s = {'a', 'b', 'c', 'd'}
print(s)  # {'a', 'c', 'd', 'b'}

s.add('a')
print(s)  # {'b', 'c', 'a', 'd'}
s.add('e')
print(s)  # {'e', 'a', 'c', 'd', 'b'}

d = {}
print(type(d))  # <class 'dict'>
s1 = set()
s2 = {'banana', 'apple'}
print(type(s1))  # <class 'set'>
print(type(s2))  # <class 'set'>

for i in {1, 2, 4, 8, 16, 32}:
    print(i)
# 32
# 1
# 2
# 4
# 8
# 16

print('apple' in s2)  # True
print('strawberry' in s2)  # False

s2.add('lemon')
s2.add('apple')
print(s2)  # {'banana', 'lemon', 'apple'}

s2.update(['melon', 'strawberry', 'orange'])
print(s2)  # {'strawberry', 'banana', 'lemon', 'melon', 'orange', 'apple'}

s2.remove('apple')
print(s2)  # {'melon', 'orange', 'banana', 'strawberry', 'lemon'}
# s2.remove('watermelon')  # KeyError: 'watermelon'

s2.discard('orange')
s2.discard('watermelon')
print(s2)  # {'lemon', 'melon', 'strawberry', 'banana'}
