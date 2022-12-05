def read_input(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def solve(lines):
    # 1 for Rock
    # 2 for Paper
    # 3 for Scissors

    d = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }

    d2 = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    total = 0

    for line in lines:
        p1, p2 = line.split(' ')
        p2 = d[p2]

        if p1 == 'A' and p2 == 'A':
            total += 3
        elif p1 == 'A' and p2 == 'B':
            total += 6
        elif p1 == 'A' and p2 == 'C':
            total += 0
        elif p1 == 'B' and p2 == 'A':
            total += 0
        elif p1 == 'B' and p2 == 'B':
            total += 3
        elif p1 == 'B' and p2 == 'C':
            total += 6
        elif p1 == 'C' and p2 == 'A':
            total += 6
        elif p1 == 'C' and p2 == 'B':
            total += 0
        elif p1 == 'C' and p2 == 'C':
            total += 3

        total += d2[p2]

    return total

def solve2(lines):
    # 1 for Rock
    # 2 for Paper
    # 3 for Scissors

    d = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    total = 0

    for line in lines:
        p1, p2 = line.split(' ')

        if p2 == 'X':
            if p1 == 'A':
                total += d['C']
            elif p1 == 'B':
                total += d['A']
            elif p1 == 'C':
                total += d['B']
        elif p2 == 'Y':
            total += 3
            total += d[p1]
        elif p2 == 'Z':
            total += 6
            if p1 == 'A':
                total += d['B']
            elif p1 == 'B':
                total += d['C']
            elif p1 == 'C':
                total += d['A']

    return total

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 15
    actual = solve(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 13924
    actual = solve(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')

    lines = read_input('input.txt')
    expected = 13448
    actual = solve2(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')