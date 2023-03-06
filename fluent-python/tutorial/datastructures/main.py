# list
arr = list([1, 2, 3])

arr.append(4)
print(arr)  # [1, 2, 3, 4]

arr.extend(["hello", "world"])
print(arr)  # [1, 2, 3, 4, 'hello', 'world']

arr.insert(1, "insert")
print(arr)  # [1, 'insert', 2, 3, 4, 'hello', 'world']

arr.remove(1)
print(arr)  # ['insert', 2, 3, 1, 4, 'hello', 'world']

arr.pop()
print(arr)  # ['insert', 2, 3, 4, 'hello']
arr.pop(2)
print(arr)  # ['insert', 2, 4, 'hello']

print(arr.index('insert'))  # 0

print(arr.count(2))  # 1

arr.sort(key=lambda x: len(str(x)))
print(arr)  # [2, 4, 'hello', 'insert']

arr2 = arr  # 얕은 복사
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

arr.clear()
print(arr)  # []
