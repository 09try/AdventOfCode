from os import cpu_count


def get_area(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()

    area = []
    for line in lines:
        heights = []
        line = line.replace('\n', '')
        for height in line:
            heights.append(int(height))
        area.append(heights)
            
    return area

def get_risk_level(area):
    
    low_points = []
    
    for row in range(len(area)):
        for col in range(len(area[row])):
            current_point = area[row][col]
            
            # 0 is lowest and 9 is highest
            up = 10
            down = 10
            left = 10
            right = 10
            
            # adjacent points
            if row != 0:
                up = area[row - 1][col]
            if row != len(area) - 1:
                down = area[row + 1][col]
            if col != 0:
                left = area[row][col - 1]
            if col != len(area[row]) - 1:
                right = area[row][col + 1]
                
            
            if current_point < up and current_point < down and current_point < left and current_point < right:
                low_points.append(current_point)
        
    
    return sum([x + 1 for x in low_points])

def check_basin(area, row, col, already_checked_points):
    
    current_basin = []
    
    examining_point = area[row][col]
    
    print('point {} at row {}, col {}'.format(examining_point, row, col))

    low_point_row_for_up = row - 1
    low_point_row_for_down = row + 1
    low_point_col_for_left = col - 1
    low_point_col_for_right = col + 1
    
    # up
    if low_point_row_for_up != -1:
        while low_point_row_for_up != 0:
            point = area[low_point_row_for_up][col]
            
            if (low_point_row_for_up, col) in already_checked_points:
                break
            
            if point != 9:
                current_basin.append(point)
                
                already_checked_points.append((low_point_row_for_up, col))
                t = check_basin(area, low_point_row_for_up, col, already_checked_points)
                
                if t != []:
                    current_basin = current_basin + t
            else:
                break
            low_point_row_for_up -= 1
    
    # down
    if low_point_row_for_down < len(area) - 1:
        while low_point_row_for_down != (len(area) - 1):
            point = area[low_point_row_for_down][col]
            
            if (low_point_row_for_down, col) in already_checked_points:
                break
            
            if point != 9:
                current_basin.append(point)
                
                already_checked_points.append((low_point_row_for_down, col))
                t = check_basin(area, low_point_row_for_down, col, already_checked_points)
                
                if t != []:
                    current_basin = current_basin + t
            else:
                break
            low_point_row_for_down += 1
            
    # left 
    if low_point_col_for_left != -1:
        while low_point_col_for_left != -1:
            point = area[row][low_point_col_for_left]
            
            if (row ,low_point_col_for_left) in already_checked_points:
                break
            
            if point != 9:
                current_basin.append(point)
                
                already_checked_points.append((row ,low_point_col_for_left))
                t = check_basin(area, row, low_point_col_for_left, already_checked_points)
                
                if t != []:
                    current_basin = current_basin + t
            else:
                break
            low_point_col_for_left -= 1
    
    # right
    if low_point_col_for_right != len(area[row]) - 1:
        while low_point_col_for_right != len(area[row]):
            point = area[row][low_point_col_for_right]
            
            if (row, low_point_col_for_right) in already_checked_points:
                break
            
            if point != 9:
                current_basin.append(point)
                
                already_checked_points.append((row, low_point_col_for_right))
                t = check_basin(area, row, low_point_col_for_right, already_checked_points)
                
                if t != []:
                    current_basin = current_basin + t
            else:
                break
            low_point_col_for_right += 1
            
    return current_basin

def get_three_largest_basins(area):

    low_points = []
    basins = []

    for row in range(len(area)):
        for col in range(len(area[row])):
            current_point = area[row][col]

            # 0 is lowest and 9 is highest
            up = 10
            down = 10
            left = 10
            right = 10

            # adjacent points
            if row != 0:
                up = area[row - 1][col]
            if row != len(area) - 1:
                down = area[row + 1][col]
            if col != 0:
                left = area[row][col - 1]
            if col != len(area[row]) - 1:
                right = area[row][col + 1]


            if current_point < up and current_point < down and current_point < left and current_point < right:
                low_points.append(current_point)
                
                # find basin
                current_basin = []
                current_basin.append(current_point)
                
                already_checked_points = []
                already_checked_points.append((row, col))
                
                current_basin = current_basin + check_basin(area, row, col, already_checked_points)
                
                basins.append(len(current_basin))


    
    three_largest_basins = sorted(basins)[-3:]
    
    return three_largest_basins[0] * three_largest_basins[1] * three_largest_basins[2]
    
if __name__ == '__main__':
    
    expected = 15
    test_area = get_area('test_input.txt')
    risk_level = get_risk_level(test_area)
    print(risk_level)
    if risk_level == expected:
        print('ok')
    else:
        print('error')
    
    expected = 502
    area = get_area('input.txt')
    risk_level  = get_risk_level(area)
    print(risk_level)
    if risk_level == expected:
        print('ok')
    else:
        print('error')
        
    expected = 1134
    result = get_three_largest_basins(test_area)
    print(result)
    if result == expected:
        print('ok')
    else:
        print('error')