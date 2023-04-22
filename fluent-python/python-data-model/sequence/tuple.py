lax_coordinates = tuple([33.9425, -118.408058])  # 로스엔젤레스 국제공항의 위도, 경도
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 도쿄에 대한 데이터 (지명, 년도, 백만 단위 인구수, 인구 변화율, 제곱킬로미터 단위 면적)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]  # 국가코드, 여권번호

for passport in traveler_ids:
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)

print(city)
print(year)
print(pop)
print(chg)
print(area)

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
