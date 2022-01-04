def read_instructions(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    
    fold_instructions = []
    _paper = []
    max_x = 0
    max_y = 0
    for line in lines:
        try:
            _ = int(line[0])
            split_result = line.replace('\n', '').split(',')
            x = int(split_result[0])
            y = int(split_result[1])
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            _paper.append([x, y])
        except:
            if line[0] == 'f':
                line = line.replace('\n', '')
                fold_instructions.append((line[-3], int(line[-1])))
    paper = []
    for _ in range(max_x + 1):
        row = []
        for _ in range(max_y + 1):
            row.append('.')
        paper.append(row)
        
    for dot in _paper:
        paper[dot[0]][dot[1]] = '#'
            
    return fold_instructions, paper

if __name__ == '__main__':
    
    fold_instructions, paper = read_instructions('test_input.txt')
    
    
    print()