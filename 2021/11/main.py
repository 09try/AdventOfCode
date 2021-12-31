def get_grid(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    
    return [[int(x) for x in line.replace('\n', '')] for line in lines]

def get_count_of_flashes(grid, steps):
    
    flashes_count = 0
    
    for row in range(len(grid)):
        r = ''
        for col in range(len(grid[0])):
            r += str(grid[row][col]) + ' '
        print(r)
    
    return flashes_count

if __name__ == '__main__':
    
    
    test_grid = get_grid('test_input.txt')
    steps = 100
    expected = 1656
    flashes_count = get_count_of_flashes(test_grid, steps)
    if flashes_count == expected:
        print('ok')
    else:
        print('error')
        
        
    grid = get_grid('input.txt')
    steps = 100
    flashes_count = get_count_of_flashes(grid, steps)
    print(flashes_count)
    