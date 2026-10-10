a = int(input('Time with river: '))
b = int(input('Time against river: '))
c = int(input('Distance: '))
v1 = c/a
v2 = c/b
v = (v1+v2)/2
u = (v1-v2)/2
print(f'Boat: {v}, River: {u}')