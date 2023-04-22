## Sequence (자료형)

### 내장 시퀀스

파이썬 표준 라이브러리는 두가시 시퀀스형을 제공한다.

1. 컨테이너 시퀀스  
    서로다른 자료형의 항목들을 담을 수 있는 자료형  
    예) list, tuple, collections.deque 형
2. 균일 시퀀스  
   단 하나의 자료형만 담을 수 있는 자료형
   예) str, bytes, bytearray, memoryview, array.array 형

### List Comprehension (지능형 리스트)

list comprehension은 리스트를 쉽고 짧게 만들어주는 파이썬 문법이다.
list comprehension의 기본 문법은 다음과 같다.
```
[(변수를 활용한 값) for (변수) in (순회가 가능한 값)]
```
1부터 10까지 값에 2를 곱한 값을 가지는 배열을 만드는 예
```python
# 일반적인 리스트 생성
arr = []
for num in range(1, 10):
    arr.append(num)
print(arr)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension
arr = [num for num in range(1, 11)]
print(arr)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

list comprehension을 사용하여 데카르트 곱 구해보기
```python
colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']
tshirt1 = []
for size in sizes:
    for color in colors:
        tshirt1.append((size, color))
print(tshirt1)
# [('S', 'Red'), ('S', 'Blue'), ('M', 'Red'), ('M', 'Blue'), ('L', 'Red'), ('L', 'Blue')]

tshirt2 = [(size, color) for size in sizes for color in colors]
print(tshirt2)
# [('S', 'Red'), ('S', 'Blue'), ('M', 'Red'), ('M', 'Blue'), ('L', 'Red'), ('L', 'Blue')]
```
두 코드의 결과는 동일한 결과를 반환한다.

### Generator expressions

제너레이터 표현식은 반복자 프로토콜을 사용하여 항목을 한개씩 생성하며 이는 메모리를 더 적게 사용한다.
또한 제너레이터 표현식은 지능형 리스트와 동일한 문법을 사용하지만 괄호를 사용한다.

```python
colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']
for tshirt in (f"{size}, {color}" for size in sizes for color in colors):
    print(tshirt)
# S, Red
# S, Blue
# M, Red
# M, Blue
# L, Red
# L, Blue
```
제너레이터 표현식은 한번에 한가지의 항목을 생성하며 6개 티셔츠의 종류를 담는 리스트를 반환하지 않는다.

### tuple

#### 레코드로서의 튜플

튜플은 레코드를 담고 있으며 각 항목은 레코드의 필드 하나를 의미하고 항목의 위치가 의미를 결정한다.

튜플은 불변 객체인데 이를 필드명이 없는 레코드로 사용시에는 튜플을 정렬하면 튜플 레코드 각 항목의 의미가 파괴될 수 있다.

```python
lax_coordinates = tuple([33.9425, -118.408058])  # 로스엔젤레스 국제공항의 위도, 경도
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 도쿄에 대한 데이터 (지명, 년도, 백만 단위 인구수, 인구 변화율, 제곱킬로미터 단위 면적)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]  # 국가코드, 여권번호

for passport in traveler_ids:
    print("%s/%s" % passport)
# USA/31195855
# BRA/CE342567
# ESP/XDA205856

for country, _ in traveler_ids:
    print(country)
# USA
# BRA
# ESP

print(city)  # Tokyo
print(year)  # 2003
print(pop)  # 32450
print(chg)  # 0.66
print(area)  # 8014
```

#### 튜플 언패킹
튜플 언패킹은 반복 가능한 객체라면 어떤 객체든 적용이 가능하다.

튜플 언패킹은 다음과 같이 활용이 가능하다.

```python
num1 = 1
num2 = 2
num1, num2 = num2, num1
print(num1)  # 2
print(num2)  # 1

print(divmod(20, 8))  # (2, 4)
t = (20, 8)
print(divmod(*t))  # (2, 4)
quotient, remainder = divmod(20, 8)
print(quotient)  # 2
print(remainder)  # 4

import os
_, filename = os.path.split("/usr/app/src/main.py")
print(filename)  # main.py
```
튜플 언패킹을 활용하면 임시변수를 사용하지 않아도 두 변수의 값을 교환할 수 있고  
함수의 반환값을 각각의 변수에 할당이 가능하다.

또한 튜플에 내포된 튜플을 언패킹도 가능하다.

```python
metro_address = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'In', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'Mx', 20.142, (19.433333, -99.133333)),
]

print("{:15} | {:^9} | {:^9}".format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, _, _, (lat, long) in metro_address:
    print(fmt.format(name, lat, long))
#                 |   lat.    |   long.  
# Tokyo           |   35.6897 |  139.6917
# Delhi NCR       |   28.6139 |   77.2089
# Mexico City     |   19.4333 |  -99.1333
```

#### namedtuple
collections.namedtuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성한다.

```python
from collections import namedtuple
City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo.name)  # Tokyo
print(tokyo.coordinates)  # (35.689722, 139.691667)

print(City._fields)
# ('name', 'country', 'population', 'coordinates')
LatLong = namedtuple("LatLong", 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613899, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
# {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': LatLong(lat=28.613899, long=77.208889)}

for key, value in delhi._asdict().items():
    print(key + ':', value)
# name: Delhi NCR
# country: IN
# population: 21.935
# coordinates: LatLong(lat=28.613899, long=77.208889)
```
