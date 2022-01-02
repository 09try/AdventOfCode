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
    
def get_count_of_flashes(grid, steps):
    flashes_count = 0
    
    #print('before any steps')
    #print_grid(grid)
    
    for step in range(steps):

        # first increase all energy levels
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] += 1
                
        coords_to_flash = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 9:
                    coords_to_flash.append((row, col))   
        
        flashed_coords = []
        while coords_to_flash != []:
            for coord in coords_to_flash:
                row = coord[0]
                col = coord[1]
                coords_to_flash.remove(coord)
                flashed_coords.append(coord)
                
                # update adjacent coords
                up = False
                down = False
                left = False
                right = False
                
                # up
                if row - 1 >= 0:
                    grid[row - 1][col] += 1
                    up = True
                    
                    if grid[row - 1][col] > 9:
                        if (row - 1, col) not in flashed_coords and (row - 1, col) not in coords_to_flash:
                            coords_to_flash.append((row - 1, col))
                    
                # down
                if row + 1 < len(grid):
                    grid[row + 1][col] += 1
                    down = True
                    
                    if grid[row + 1][col] > 9:
                        if (row + 1, col) not in flashed_coords and (row + 1, col) not in coords_to_flash:
                            coords_to_flash.append((row + 1, col))
                    
                # left    
                if col - 1 >= 0:
                    grid[row][col - 1] += 1
                    left = True
                    
                    if grid[row][col - 1] > 9:
                        if (row, col - 1) not in flashed_coords and (row, col - 1) not in coords_to_flash:
                            coords_to_flash.append((row, col - 1))
                    
                # right
                if col + 1 < len(grid[row]):
                    grid[row][col + 1] += 1
                    right = True
                    
                    if grid[row][col + 1] > 9:
                        if (row, col + 1) not in flashed_coords and (row, col + 1) not in coords_to_flash:
                            coords_to_flash.append((row, col + 1))
                    
                # up left
                if up and left:
                    grid[row - 1][col - 1] += 1
                    
                    if grid[row - 1][col - 1] > 9:
                        if (row - 1, col - 1) not in flashed_coords and (row - 1, col - 1) not in coords_to_flash:
                            coords_to_flash.append((row - 1, col - 1))
                    
                # up right
                if up and right:
                    grid[row - 1][col + 1] += 1
                    
                    if grid[row - 1][col + 1] > 9:
                        if (row - 1, col + 1) not in flashed_coords and (row - 1, col + 1) not in coords_to_flash:
                            coords_to_flash.append((row - 1, col + 1))
                    
                # down left
                if down and left:
                    grid[row + 1][col - 1] += 1
                    
                    if grid[row + 1][col - 1] > 9:
                        if (row + 1, col - 1) not in flashed_coords and (row + 1, col - 1) not in coords_to_flash:
                            coords_to_flash.append((row + 1, col - 1))
                    
                # down right
                if down and right:
                    grid[row + 1][col + 1] += 1
                    
                    if grid[row + 1][col + 1] > 9:
                        if (row + 1, col + 1) not in flashed_coords and (row + 1, col + 1) not in coords_to_flash:
                            coords_to_flash.append((row + 1, col + 1))
                    
        c = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 9:
                    grid[row][col] = 0
                    flashes_count += 1
                c += grid[row][col]
                
        print('after step', step + 1)
        print_grid(grid)
        
        if c == 0:
            print('all coords are synchronized')
    
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
        
    test_grid = get_grid('test_input.txt')
    steps = 100
    expected = 1656
    flashes_count = get_count_of_flashes(test_grid, steps)
    print(flashes_count)
    if flashes_count == expected:
        print('ok')
    else:
        print('error')
        
        
    grid = get_grid('input.txt')
    steps = 100
    expected = 1673
    flashes_count = get_count_of_flashes(grid, steps)
    print(flashes_count)
    if flashes_count == expected:
        print('ok')
    else:
        print('error')
        
    grid = get_grid('input.txt')
    steps = 279
    expected = 1673
    flashes_count = get_count_of_flashes(grid, steps)
    print(flashes_count)
    if flashes_count == expected:
        print('ok')
    else:
        print('error')
    