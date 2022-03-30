def read_input(path):
    f = open(path, 'r')
    lines = [line.strip().replace('\n', '') for line in f.readlines()]
    f.close()
    
    return [[int(risk_level) for risk_level in line] for line in lines]
    
def get_optimal_path_risk_level(cavern):
    
    path = []
    path.append([0, 0])
    
    row = 0
    col = 0
    
    while row != 9 and col != 9:
            
        risk_level_up = 10
        risk_level_down = -1
        risk_level_left = -1
        risk_level_right = -1
        
        # pridat kriterium celkovy risk level, nie len aktualny left, right, down, up
        
        # # up
        # if row - 1 >= 0:
        #     risk_level_up = cavern[row - 1][col]
        
        # down
        if row + 1 < len(cavern[0]):
            risk_level_down = cavern[row + 1][col]
        
        # left
        if col - 1 >= 0:
            risk_level_left = cavern[row][col - 1]
        
        # right
        if col + 1 < len(cavern):
            risk_level_right = cavern[row][col + 1]
            
        p = [('up', risk_level_up)]
        
        if [row + 1, col] not in path and risk_level_down != -1:
            p.append(('down', risk_level_down))
            
        if [row, col - 1] not in path and risk_level_left != -1:
            p.append(('left', risk_level_left))
            
        if [row, col + 1] not in path and risk_level_right != -1:
            p.append(('right', risk_level_right))
            
        min = 0
        for i in range(len(p)):
            if p[i][1] < p[min][1]:
                min = i
                
        dir = p[min][0]
                
        if dir == 'up':
            path.append([row - 1, col])
            row -= 1
        elif dir == 'down':
            path.append([row + 1, col])
            row += 1
        elif dir == 'left':
            path.append([row, col - 1])
            col -= 1
        elif dir == 'right':
            path.append([row, col + 1])
            col += 1
                
    print()
            

if __name__ == '__main__':
    
    cavern = read_input('test_input.txt')
    expected = 40
    total_risk = get_optimal_path_risk_level(cavern)
    
    if total_risk == expected:
        print('ok')
    else:
        print('fail')