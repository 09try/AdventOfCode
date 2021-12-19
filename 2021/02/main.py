f = open('input.txt', 'r')
planned_course = []
for line in f:
    planned_course.append(line)
    
f.close()

horizontal_position = 0
depth = 0
aim = 0

# forward -> increase horizontal position
# down -> increase depth
# up -> decrease depth

for command in planned_course:
    _command, value = command.split(' ')

    if _command == 'forward':
        horizontal_position = horizontal_position + int(value)
        depth = depth + (aim * int(value))
    elif _command == 'down':
        aim = aim + int(value)
    elif _command == 'up':
        aim = aim - int(value)

print(horizontal_position * depth)