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

if __name__ == '__main__':
    
    expected = 15
    area = get_area('test_input.txt')
    risk_level = get_risk_level(area)
        
    if risk_level == expected:
        print('ok')
    else:
        print('error')
        
    
    area = get_area('input.txt')
    risk_level  = get_risk_level(area)
    print(risk_level)
    