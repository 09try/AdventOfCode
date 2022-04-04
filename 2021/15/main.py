import sys

def read_input(path):
    f = open(path, 'r')
    lines = [line.strip().replace('\n', '') for line in f.readlines()]
    f.close()
    
    return [[int(risk_level) for risk_level in line] for line in lines]
    
def get_optimal_path_risk_level(cavern):
    
    start = [0, 0]
    end = [9, 9]
    
    all_paths = get_all_paths(cavern, start, end, [start])
    
    min_risk_level = sys.maxint
    for path in all_paths:
        current_score = 0
        for coord in path:
            current_score += cavern[coord[0], coord[1]]
        if current_score < min_risk_level:
            min_risk_level = current_score
            
    return current_score

def get_all_paths(cavern, current_pos, end, current_path):
    if current_pos == end:
        return [end]
    else:
        neighbours = [[-1, 0], [1, 0], [0, 1], [0 -1]]
        for neighbour in neighbours:
            row = current_pos[0] + neighbour[0]
            col = current_pos[1] + neighbour[1]
            
            if [row, col] not in current_path:
                if row >= 0 and row < len(cavern):
                    if col >= 0 and col < len(cavern[0]):
                        current_path.append([row, col])
                        return [row, col] + get_all_paths(cavern, [row, col], end, current_path)
            
            

if __name__ == '__main__':
    
    cavern = read_input('test_input.txt')
    expected = 40
    total_risk = get_optimal_path_risk_level(cavern)
    
    if total_risk == expected:
        print('ok')
    else:
        print('fail')