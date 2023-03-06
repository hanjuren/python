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

### 함수 정의
```python
def fib(num):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(100)
```
def 키워드로 함수 정의를 시작.
첫 라인은 문자열 리터럴이 허용됨. 여기서 작성된 문자열은 함수의 docstring 으로 적용됨.
함수로 전달되는 인자들은 값에 의한 호출(call by value)로 전달됨 (immutable 타입의 객체인 경우 한정)

> call by value?  
> 함수 호출시 전달되는 변수의 값을 복사하여 인자로 전달하는 방식으로  
> 함수의 내부에서 값이 변경되어도 원본 데이터의 값은 변하지 않는 방식이다.


#### 함수 호출시 기본 인자 지정
함수 정의시 전달 받을 인자들의 기본값을 지정하면 정의된 값보다 적은 인자를 전달해도 함수가 실행된다.
```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        print(ok)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        print(retries)
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok("Would you like to finish? y/n: ")
ask_ok("Would you like to finish? y/n: ", 2)
ask_ok("Would you like to finish? y/n: ", 2, "try again!!!")
```
인자의 기본값 사용시 주의점.
기본값이 mutable한 객체의 경우 호출시마다 새로운 값을 생성하는 것이 아닌 함수내부의 객체를 생성해두고 공유한다.
```python
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]


def f2(num=3):
    num += 1
    return num


print(f2(1))  # 2
print(f2(1))  # 2
print(f2(1))  # 2
```
두 함수 모두 기본값을 사용하여 함수내에서 값을 변경했지만 mutable한 list객체는 공유되어 원하지 않는 방식으로 동작할 가능성이 크다.

#### 키워드 인자
함수로 인자 전달 시 key=value 형식으로 인자 전달이 가능하다.
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(1000, state="hello world")
parrot(voltage=1000, action="run")
```
parrot 함수는 voltage라는 필수 인자 한개와 state, action, type 3가지의 선택적 인자를 가진 함수이다.
key=value 형식으로 인자 정의 순서와 관계없이 원하는 인자의 값으로 전달이 가능하다.