def read_input(path):
    f = open(path, 'r')
    lines = [line.strip('\n') for line in f.readlines()]
    f.close()

    for line in lines:
        tmp = line.split(' ')
        print(len(tmp), tmp)


    return lines

def solve(lines):
    return 1

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 0
    actual = solve(lines)
    #print(actual)
    
    # if expected == actual:
    #     print('ok')
    # else:
    #     print('fail')
        
    # lines = read_input('input.txt')
    # expected = 0
    # actual = solve(lines)
    # print(actual)
    
    # if expected == actual:
    #     print('ok')
    # else:
    #     print('fail')