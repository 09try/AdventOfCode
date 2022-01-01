def get_grid(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    
    return [[int(x) for x in line.replace('\n', '')] for line in lines]

def print_grid(grid):
    r = ''
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            r += str(grid[row][col]) + ' '
        r += '\n'
    print(r)
    
def flash_coordinates(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 9:
                
                # update adjacent coords
                up = False
                down = False
                left = False
                right = False

                # up
                if row - 1 >= 0:
                    grid[row - 1][col] += 1
                    up = True
                
                # down
                if row + 1 < len(grid):
                    grid[row + 1][col] += 1
                    down = True
                
                # left    
                if col - 1 >= 0:
                    grid[row][col - 1] += 1
                    left = True
                
                # right
                if col + 1 < len(grid[row]):
                    grid[row][col + 1] += 1
                    right = True
                
                # up left
                if up and left:
                    grid[row - 1][col - 1] += 1
                    
                # up right
                if up and right:
                    grid[row - 1][col + 1] += 1
                    
                # down left
                if down and left:
                    grid[row + 1][col - 1] += 1
                
                # down right
                if down and right:
                    grid[row + 1][col + 1] += 1
                        
    return grid
    
def get_count_of_flashes(grid, steps):
    flashes_count = 0
    
    print('before any steps')
    print_grid(grid)
    
    for step in range(steps):

        # first increase all energy levels
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] += 1
         
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 9:
                    grid[row][col] = 0
                    flashes_count += 1
                       
        print('after step', step + 1)
        print_grid(grid)
    
    return flashes_count

if __name__ == '__main__':
    
    test_grid = get_grid('test_input.txt')
    steps = 10
    expected = 204
    flashes_count = get_count_of_flashes(test_grid, steps)
    print(flashes_count)
    if flashes_count == expected:
        print('ok')
    else:
        print('error')
        
    # steps = 100
    # expected = 1656
    # flashes_count = get_count_of_flashes(test_grid, steps)
    # print(flashes_count)
    # if flashes_count == expected:
    #     print('ok')
    # else:
    #     print('error')
        
        
    # grid = get_grid('input.txt')
    # steps = 100
    # flashes_count = get_count_of_flashes(grid, steps)
    # print(flashes_count)
    