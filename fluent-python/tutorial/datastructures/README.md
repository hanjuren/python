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