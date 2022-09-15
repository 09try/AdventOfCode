def read_input(path):
    f = open(path, 'r')
    lines = [int(line.strip()) for line in f.readlines()]
    f.close()
    return lines

def solve(lines):
    total = 0
    for line in lines:
        total += line // 3 - 2
    return total

def calc(n):
    if n <= 0:
        return 0
    else:
        return n + calc(n // 3 - 2)

def solve2(lines):
    total = 0
    for line in lines:
        total += calc(line // 3 - 2)
        
    return total

if __name__ == '__main__':        
    lines = read_input('input.txt')
    expected = 3275518
    actual = solve(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')

    expected = 4910404
    actual = solve2(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')