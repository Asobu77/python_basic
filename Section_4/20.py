# リストの使いどころ
seat = []
min = 0
max = 5

print(min <= len(seat) < max)

seat.append('a')
seat.append('b')
seat.append('c')
seat.append('d')
seat.append('e')

print(min <= len(seat) < max)

seat.pop(0)
print(seat)

print(min <= len(seat) < max)
