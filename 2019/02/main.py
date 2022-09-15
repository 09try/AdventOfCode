def read_input(path):
    f = open(path, 'r')
    line = [int(x) for x in f.readline().strip().split(',')]
    f.close()
    return line

def solve(line):
    for i in range(0, len(line), 4):
        if line[i] == 1:
            line[line[i + 3]] = line[line[i + 1]] + line[line[i + 2]]
        if line[i] == 2:
            line[line[i + 3]] = line[line[i + 1]] * line[line[i + 2]]
        if line[i] == 99:
            return line
    
if __name__ == '__main__':
    line = read_input('test_input.txt')
    expected = 0
    actual = solve(line)
    print(actual)
    
    line = read_input('input.txt')
    expected = 6730673
    line[1] = 12
    line[2] = 2
    actual = solve(line)
    if actual[0] == expected:
        print('ok')
    else:
        print('fail')
        
    expected = 19690720
    for n1 in range(100):
        for n2 in range(100):
            line = read_input('input.txt')
            line[1] = n1
            line[2] = n2
            actual = solve(line)
            if actual[0] == expected:
                print(100 * n1 + n2)