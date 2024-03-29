def read_input(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    res = []
    for line in lines:
        split_res = line.split(',')
        curr = []
        for sr in split_res:
            tmp = sr.split('-')
            curr.append([int(tmp[0]), int(tmp[1])])
        res.append(curr)

    return res

def solve(lines):
    res = 0

    for (x1, y1), (x2, y2) in lines:
        if x2 >= x1 and y2 <= y1 or x1 >= x2 and y1 <= y2:
            res += 1

    return res

def solve2(lines):
    res = 0

    for (x1, y1), (x2, y2) in lines:
        if x1 > x2:
            if y2 >= x1:
                res += 1    
        else:
            if y1 >= x2:
                res += 1

    return res

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 2
    actual = solve(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 530
    actual = solve(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')

    lines = read_input('test_input.txt')
    expected = 4
    actual = solve2(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')

    lines = read_input('input.txt')
    expected = 903
    actual = solve2(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')