f = open('input.txt', 'r')
lines = f.readlines()
f.close()

x1 = []
y1 = []
x2 = []
y2 = []

for line in lines:
    numbers = line.split('->')
    _x1, _y1 = numbers[0].split(',')
    _x2, _y2 = numbers[1].split(',')
    x1.append(int(_x1))
    y1.append(int(_y1))
    x2.append(int(_x2))
    y2.append(int(_y2))

min_x1 = min(x1)
min_y1 = min(y1)
min_x2 = min(x2)
min_y2 = min(y2)

max_x1 = max(x1)
max_y1 = max(y1)
max_x2 = max(x2)
max_y2 = max(y2)

start_x = min(min_x1, min_x2)
start_y = min(min_y1, min_y2)

end_x = max(max_x1, max_x2)
end_y = max(max_y1, max_y2)

# create space
space = []
for row in range(end_y + 1):
    _row = []
    for col in range(end_x + 1):
        _row.append('.')
    space.append(_row)

# create diagram

for i in range(len(x1)):
    _x1 = x1[i]
    _y1 = y1[i]
    _x2 = x2[i]
    _y2 = y2[i]

    if _x1 == _x2:

        y1_it = _y1
        y2_it = _y2

        if _y1 > _y2:
            y1_it = _y2
            y2_it = _y1

        for __y in range(y1_it, y2_it + 1):
            if space[__y][_x1] == '.':
                space[__y][_x1] = 1
            else:
                space[__y][_x1] += 1

    if _y1 == _y2:

        x1_it = _x1
        x2_it = _x2

        if _x1 > _x2:
            x1_it = _x2
            x2_it = _x1

        for __x in range(x1_it, x2_it + 1):
            if space[_y1][__x] == '.':
                space[_y1][__x] = 1
            else:
                space[_y1][__x] += 1

c = 0
for row in range(end_y + 1):
    for col in range(end_x + 1):
        if space[row][col] != '.' and space[row][col] > 1:
            c += 1

print(c)