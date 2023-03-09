t = 10000, 10001, 10002
print(t)  # (10000, 10001, 10002)
print(t[1])  # 10001

# tuple is immutable
# t[1] = 11111  # TypeError: 'tuple' object does not support item assignment

t1 = ()
print(t1)  # ()

t2 = (1111,)
print(t2)  # (1111,)

t3 = 1111, 1111, 1111
print(t3)  # (1111, 1111, 1111)
