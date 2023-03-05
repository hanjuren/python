## 제어문

### if 문
```python
x = int(input("Please enter an integer: "))
# Please enter an integer: 2

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# More
```

### for 문
```python
users = {'Han': 'active', 'Yang': 'inactive', 'Kim': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)  # {'Han': 'active', 'Kim': 'active'}

users = {'Han': 'active', 'Yang': 'inactive', 'Kim': 'active'}
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(users)  # {'Han': 'active', 'Yang': 'inactive', 'Kim': 'active'}
print(active_users)  # {'Han': 'active', 'Kim': 'active'}
```

> 숫자들의 시퀀스로 반복할 필요가 있다면 range 함수를 사용 하면 편하다.  
> ```python
> for n in range(5):
>   print(n)
> 
> # 0
> # 1
> # 2
> # 3
> # 4
> ```

### loop break, continue and else
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # for 문의 else 는 break 가 실행 되지 않을때 실행됨.
        print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
```

### pass 문
pass문은 아무것도 하지 않는다. 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 사용

### match 문

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
3.10 부터 지원 이전 버전은 switch 문이 없다. 그냥 if..else 혹은 dictionary 사용하는 방식도 있다.