def get_grid(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    
    return [[int(x) for x in line.replace('\n', '')] for line in lines]

def print_grid(grid):
    r = ''
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            r += str(grid[row][col]).zfill(3) + ' '
        r += '\n'
    print(r)
    
def update_energy_levels(grid):
    new_grid = grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            new_grid[row][col] += 1
            
    return new_grid

def get_count_of_flashes(grid, steps):
    
    flashes_count = 0
    
    print_grid(grid)
    
    for _ in range(steps):
        
        # first increase all energy levels
        new_grid = update_energy_levels(grid)
        
        # if grid[row][col] > 9:
        #     coordinates_to_flash.append([row, col])
                
        # # energy levels greater than 9 flash
        # for coord in coordinates_to_flash:
        #     row = coord[0]
        #     col = coord[1]
        #     grid[row][col] = 0
            
        #     # increase adjacent octopuses
        #     up = False
        #     down = False
        #     left = False
        #     right = False
            
        #     # up
        #     if row - 1 >= 0:
        #         grid[row - 1][col] += 1
        #         up = True
        #     # down
        #     if row + 1 < len(grid):
        #         grid[row + 1][col] += 1
        #         down = True
        #     # left    
        #     if col - 1 <= len(grid[row]):
        #         grid[row][col - 1] += 1
        #         left = True
        #     # right
        #     if col + 1 < len(grid[row]):
        #         grid[row][col + 1] += 1
        #         right = True
        #     # up left
        #     if up and left:
        #         grid[row - 1][col - 1] += 1
        #     # up right
        #     if up and right:
        #         grid[row - 1][col + 1] += 1
        #     # down left
        #     if down and left:
        #         grid[row + 1][col - 1] += 1
        #     # down right
        #     if down and right:
        #         grid[row + 1][col + 1] += 1
            
        # # check again which should flash but don't flash the same twice
        # for coord in coords_increased:
        #     if coord not in coordinates_to_flash:
        #         row = coord[0]
        #         col = coord[1]
        #         if grid[row][col] > 9:
        #             grid[row][col] = 0
                    
        #             # increase adjacent octopuses
        #             # ...
        
        
        print_grid(new_grid)
    
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
        
        
    # grid = get_grid('input.txt')
    # steps = 100
    # flashes_count = get_count_of_flashes(grid, steps)
    # print(flashes_count)
    