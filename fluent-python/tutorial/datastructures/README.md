### 리스트 자료형 메서드

#### 1. list.append(x)
리스트의 마지막에 값을 추가.
```python
arr = list()
arr.append(4)
print(arr)  # [1, 2, 3, 4]
```

#### 2. list.extend(list)
리스트에 인자로 전달된 리스트의 모든 값을 추가.
```python
arr = list([1, 2, 3, 4])
arr.extend(["hello", "world"])
print(arr)  # [1, 2, 3, 4, 'hello', 'world']
```

#### 3. list.insert(idx, value)
첫번쨰 인자로 전달된 값의 인덱스에 해당하는 위치에 값을 추가
```python
arr = [1, 2, 3, 4, 'hello', 'world']
arr.insert(1, "insert")
print(arr)  # [1, 'insert', 2, 3, 4, 'hello', 'world']
```

#### 4. list.remove(value)
인자로 전달된 값과 일치하는 첫번쨰 값을 리스트에서 제거  
일치하는 값이 없을경우 ValueError 발생
```python
arr = [1, 'insert', 2, 3, 4, 'hello', 'world']
arr.remove(1)
print(arr)  # ['insert', 2, 3, 1, 4, 'hello', 'world']

arr.remove("value error")
# ValueError: list.remove(x): x not in list
```

#### 5. list.pop([idx])
선택적 인자로 인자를 전달하지 않은 경우 리스트의 맨 마지막 인덱스의 값이 제거하고 제거된 항목을 리턴  
인자로 인덱스를 전달하면 해당 위치의 값을 제거하고 제거한 값을 리턴한다.
```python
arr = ['insert', 2, 3, 1, 4, 'hello', 'world']
arr.pop()
print(arr)  # ['insert', 2, 3, 4, 'hello']
arr.pop(2)
print(arr)  # ['insert', 2, 4, 'hello']
```

#### 6. list.index(x[, start[, end]])
리스트의 항목 중 x와 일치하는 값의 첫번째 인덱스를 리턴하고 값이 없을 경우 ValueError 발생  
start, end 인자 전달시 해당 인자들은 슬라이스 표기법처럼 인식된다.
```python
arr = ['insert', 2, 4, 'hello']
print(arr.index('insert'))  # 0
```

#### 7. list.count(x)
리스트에 x값의 갯수를 리턴
```python
arr = ['insert', 2, 4, 'hello']
print(arr.count(2))  # 1
```

#### 8. list.sort(*, key=None, reverse=False)
리스트의 항목들을 정렬 reverse=True 시 역방향 정렬
```python
arr = ['insert', 2, 4, 'hello']
arr.sort(key=lambda x: len(str(x)))  # [2, 4, 'hello', 'insert']
```

#### 9. list.copy()
리스트 복사  
copy 메서드로 복사된 리스트는 원본과 다른 주소를 가진 객체를 리턴한다.  
반면 = 키워드로 복사된 값은 동일한 주소를 가진 객체를 리턴한다.  
> 얕은 복사와 깊은 복사 공식문서  
> https://docs.python.org/3/library/copy.html
```python
arr = [2, 4, 'hello', 'insert']
arr2 = arr
arr3 = arr.copy()
print(id(arr))
print(id(arr2))
print(id(arr3))

arr2.append("shallow copy")
print(arr)  # [2, 4, 'hello', 'insert', 'shallow copy']
print(arr2)  # [2, 4, 'hello', 'insert', 'shallow copy']
print(arr3)  # [2, 4, 'hello', 'insert']

arr3.append("deep copy")
print(arr)  # [2, 4, 'hello', 'insert', 'shallow copy']
print(arr2)  # [2, 4, 'hello', 'insert', 'shallow copy']
print(arr3)  # [2, 4, 'hello', 'insert', 'deep copy']
```

#### list.clear()
리스트의 모든 항목을 삭제한다.
```python
arr = [2, 4, 'hello', 'insert', 'shallow copy']
arr.clear()
print(arr)  # []
```
---
### tuple
튜플은 쉼표로 구분되는 여러값으로 구성된 자료형이다.  
기본적인 구조는 다음과 같다.
```python
t = 10000, 10001, 10002
print(t)  # (10000, 10001, 10002)
print(t[1])  # 10001
```
튜플의 값은 괄호로 둘러쌓여지며 튜플은 불변한 객체이다. 튜플의 값을 변경하고자 하면 에러가 발생한다.
```python
t[1] = 11111  # TypeError: 'tuple' object does not support item assignment
```
튜플을 만들기 위해서는 다음과 같은 방식이 있다.
```python
# 비어있는 튜플
t1 = ()
print(t1)  # ()

# 값이 한개인 튜플
t2 = (1111,)
print(t2)  # (1111,)
```
또한 튜플은 튜플내 중복된 값을 허용한다.
```python
t3 = 1111, 1111, 1111
print(t3)  # (1111, 1111, 1111)
```
---
### Set
set 자료형은 tuple과 다르게 중복값이 허용되지 않는 자료형이고 중괄호로 둘러 쌓인 구조의 자료형이다.
```python
s = {'a', 'b', 'c', 'd'}
print(s)  # {'a', 'c', 'd', 'b'}
```
set 자료형 선언 방식은 set 생성자를 사용하거나 중괄호 안에 값을 넣어주면된다.  
비어있는 중괄호로 선언하게 되면 해당 자료형은 set이 아닌 dict 자료형이 된다.
```python
d = {}
print(type(d))  # <class 'dict'>
s1 = set()
s2 = {'banana', 'apple'}
print(type(s1))  # <class 'set'>
print(type(s2))  # <class 'set'>
```
set은 선언한 순서의 보장이 되지 않는다. 즉 선언한 값의 순서가 일치하지 않는다.
```python
for i in {1, 2, 4, 8, 16, 32}:
    print(i)
# 32
# 1
# 2
# 4
# 8
# 16
```
set 또한 다른 자료형과 같이 in 메서드를 사용할 수 있다.
```python
s2 = {'banana', 'apple'}
print('apple' in s2)  # True
print('strawberry' in s2)  # False
```
set 자료형에 값을 추가할땐 add 메서드를 사용한다.  
이때 이미 값이 있다면 추가 되지 않는다.
```python
s2 = {'banana', 'apple'}
s2.add('lemon')
s2.add('apple')
print(s2)  # {'banana', 'lemon', 'apple'}
```
여러개의 값을 한번에 추가하기 위해서는 update 메서드를 사용할 수 있다.
```python
s2 = {'banana', 'apple'}
s2.update(['melon', 'strawberry', 'orange'])
print(s2)  # {'strawberry', 'banana', 'lemon', 'melon', 'orange', 'apple'}
```
set의 값을 제거하기 위해서는 두가지 방식이 있다.  
1. remove(item)
remove 메서드의 인자로 값을 지정하고 해당하는 값이 set에 없는경우 KeyError가 발생한다.
```python
s2 = {'strawberry', 'banana', 'lemon', 'melon', 'orange', 'apple'}
s2.remove('apple')
print(s2)  # {'melon', 'orange', 'banana', 'strawberry', 'lemon'}
s2.remove('watermelon')  # KeyError: 'watermelon's2.remove('apple')
```
2. discard(item)
set에 값이 없어도 에러가 발생하지 않는다.
```python
s2 =  {'melon', 'orange', 'banana', 'strawberry', 'lemon'}
s2.discard('orange')
s2.discard('watermelon')
print(s2)  # {'lemon', 'melon', 'strawberry', 'banana'}
```