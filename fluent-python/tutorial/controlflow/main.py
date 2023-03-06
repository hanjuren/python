x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


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


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # for 문의 else 는 break 가 실행 되지 않을때 실행됨.
        print(n, 'is a prime number')


status_code = 400
match status_code:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapo")
    case _:
        print("Something's wrong with the internet")


def fib(num):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(100)


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


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f2(num=3):
    num += 1
    return num


print(f2(1))  # 2
print(f2(1))  # 2
print(f2(1))  # 2


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(1000, state="hello world")
parrot(voltage=1000, action="run")
