CENTRAL_PORT_ROW = 1
CENTRAL_PORT_COL = 1

def read_input(path):
    f = open(path, 'r')
    lines = [x.split(',') for x in [line.strip() for line in f.readlines()]]
    f.close()
    return lines

def get_path(directions):
    curr_row = CENTRAL_PORT_ROW
    curr_col = CENTRAL_PORT_COL
    d = {}
    steps = 0
    d[(curr_row, curr_col)] = steps
    
    for direction in directions:
        length = int(direction[1:])
        
        if direction[0] == 'R':
            for _ in range(length):
                curr_col += 1
                steps += 1
                d[(curr_row, curr_col)] = steps
                
        if direction[0] == 'L':
            for _ in range(length):
                curr_col -= 1
                steps += 1
                d[(curr_row, curr_col)] = steps
                
        if direction[0] == 'U':
            for _ in range(length):
                curr_row += 1
                steps += 1
                d[(curr_row, curr_col)] = steps
                
        if direction[0] == 'D':
            for _ in range(length):
                curr_row -= 1
                steps += 1
                d[(curr_row, curr_col)] = steps
    
    return d

def get_lowest_distance(path1, path2):
    lowest = float('inf')

    for k, _ in path1.items():
        if k in path2:
            if k != (CENTRAL_PORT_ROW, CENTRAL_PORT_COL):
                y1, x1 = CENTRAL_PORT_ROW, CENTRAL_PORT_COL
                y2, x2 = k
                distance = abs(x1 - x2) + abs(y1 - y2)
                if distance < lowest:
                    lowest = distance
        
    return lowest

def get_lowest_steps(path1, path2):
    lowest = float('inf')

    for k, _ in path1.items():
        if k in path2:
            if k != (CENTRAL_PORT_ROW, CENTRAL_PORT_COL):
                y1, x1 = CENTRAL_PORT_ROW, CENTRAL_PORT_COL
                y2, x2 = k
                distance = abs(x1 - x2) + abs(y1 - y2)
                
                steps1 = path1[k]
                steps2 = path2[k]
                
                if steps1 + steps2 < lowest:
                    lowest = steps1 + steps2
        
    return lowest
    
if __name__ == '__main__':
    
    directions1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    directions2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
    path1 = get_path(directions1)
    path2 = get_path(directions2)
    print('159', get_lowest_distance(path1, path2))
    print('610', get_lowest_steps(path1, path2))
    
    directions1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
    directions2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    path1 = get_path(directions1)
    path2 = get_path(directions2)
    print('135', get_lowest_distance(path1, path2))
    print('410', get_lowest_steps(path1, path2))
    
    directions1 = ['R8','U5','L5','D3']
    directions2 = ['U7','R6','D4','L4']
    path1 = get_path(directions1)
    path2 = get_path(directions2)
    print('6', get_lowest_distance(path1, path2))
    print('30', get_lowest_steps(path1, path2))
    
    directions1, directions2 = read_input('input.txt')
    path1 = get_path(directions1)
    path2 = get_path(directions2)
    print(get_lowest_distance(path1, path2))
    print(get_lowest_steps(path1, path2))