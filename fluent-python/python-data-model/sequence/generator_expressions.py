text = 'hello'
arr = list(t for t in text)
print(arr)

colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']
for tshirt in (f"{size}, {color}" for size in sizes for color in colors):
    print(tshirt)

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
