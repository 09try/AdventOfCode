def read_input(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def solve(lines):
    curr_max = 0
    curr = 0
    for line in lines:
        if line == '':
            curr_max = max(curr_max, curr)
            curr = 0
        else:
            curr += int(line)

    curr_max = max(curr_max, curr)

    return curr_max

def solve2(lines):
    curr_max = [0, 0, 0]
    curr = 0
    for line in lines:
        if line == '':
            curr_max = sorted(curr_max)
            if curr > curr_max[0]:
                curr_max[0] = curr
                curr = min(curr_max)
            curr = 0
        else:
            curr += int(line)

    curr_max = sorted(curr_max)
    if curr > curr_max[0]:
        curr_max[0] = curr

    return sum(curr_max)

def solve3(f):
    ff = open(f)
    data = sum(sorted([sum(n) for n in [[int(c) for c in l.split('\n')] for l in ff.read().split('\n\n')]])[-3:])
    ff.close()
    return data

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 24000
    actual = solve(lines)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 72478
    actual = solve(lines)

    if expected == actual:
        print('ok')
    else:
        print('fail')

    lines = read_input('test_input.txt')
    expected = 45000
    actual = solve2(lines)

    if expected == actual:
        print('ok')
    else:
        print('fail')

    lines = read_input('input.txt')
    expected = 210367
    actual = solve2(lines)

    if expected == actual:
        print('ok')
    else:
        print('fail')

    expected = 210367
    actual = solve3('input.txt')

    if expected == actual:
        print('ok')
    else:
        print('fail')