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
