import math

def read_input(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def solve(lines):
    highest_seat_id = 0
    
    for line in lines:
        current_seat_id = get_seat_id(line)
        
        if current_seat_id > highest_seat_id:
            highest_seat_id = current_seat_id
            
    return highest_seat_id

def solve2(lines):
    seat_ids = []
    for line in lines:
        current_seat_id = get_seat_id(line)
        seat_ids.append(current_seat_id)
        
    sorted_seat_ids = sorted(seat_ids)
    
    missing_seat_id = sorted_seat_ids[0]
    previous_seat_id = sorted_seat_ids[0]
    for current_seat_id in sorted_seat_ids[1:]:
        diff = current_seat_id - previous_seat_id
        if diff != 1:
            missing_seat_id = current_seat_id - 1
            print('previous_seat_id', previous_seat_id)
            print('current_seat_id', current_seat_id)
            print('missing_seat_id', missing_seat_id)
        previous_seat_id = current_seat_id
        
    return missing_seat_id
    
def get_seat_id(line):
    row = 0
    
    for i, n in enumerate(line[::-1][3:]):
        if n == 'B':
            row += math.pow(2, i)
            
    column = [0, 1, 2, 3, 4, 5, 6, 7]
    
    for n in line[-3:]:
        if n == 'R':
            l = int((len(column) / 2))
            column = column[l:]
            
        if n == 'L':
            l = int((len(column) / 2))
            column = column[:l]
    
    column = column[0]
    
    return int(row * 8 + column)

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 820
    actual = solve(lines)
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 989
    actual = solve(lines)
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    expected = 548
    lines = read_input('input.txt')
    actual = solve2(lines)
    print(actual)
    if expected == actual:
        print('ok')
    else:
        print('fail')