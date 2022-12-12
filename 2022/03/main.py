def read_input(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def solve(lines):
    output = 0
    lower = [x for x in range(1, 26 + 1)]
    upper = [x for x in range(27, 52 + 1)]

    for line in lines:
        l = line[:(len(line) // 2)]
        r = line[(len(line) // 2):]

        dl = {}
        for c in l:
            if c not in dl:
                dl[c] = True

        for c in r:
            if c in dl:
                if c.islower():
                    t = lower[ord(c) - ord('a')]
                    output += t
                else:
                    t = upper[ord(c) - ord('A')]
                    output += t

                del dl[c]

    return output

def solve2(lines):
    output = 0
    lower = [x for x in range(1, 26 + 1)]
    upper = [x for x in range(27, 52 + 1)]

    for i in range(0, len(lines), 3):
        d1 = {}
        d2 = {}
        d3 = {}

        m = max(len(lines[i]), len(lines[i + 1]), len(lines[i + 2]))

        for j in range(m):
            if j < len(lines[i]):
                if lines[i][j] not in d1:
                    d1[lines[i][j]] = True
            if j < len(lines[i + 1]):
                if lines[i + 1][j] not in d2:
                    d2[lines[i + 1][j]] = True
            if j < len(lines[i + 2]):
                if lines[i + 2][j] not in d3:
                    d3[lines[i + 2][j]] = True

        for k, v in d1.items():
            if k in d2 and k in d3:
                if k.islower():
                    t = lower[ord(k) - ord('a')]
                    output += t
                else:
                    t = upper[ord(k) - ord('A')]
                    output += t

    return output

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 157
    actual = solve(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 8139
    actual = solve(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')

    lines = read_input('test_input.txt')
    expected = 70
    actual = solve2(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 2668
    actual = solve2(lines)
    print(actual)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')