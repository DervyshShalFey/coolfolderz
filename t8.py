x = int(input('Objects: '))
if x%12 > 0:
    print(f'Packages: {(x//12)+1}')
else:
    print(f'Packages: {x//12}')