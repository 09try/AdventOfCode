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
    low_points = [1, 0, 5, 5]
    
    
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
    