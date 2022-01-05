def read_instructions(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    
    fold_instructions, _paper = [], []
    max_x, max_y = 0, 0
    for line in lines:
        try:
            _ = int(line[0])
            split_result = line.replace('\n', '').split(',')
            x, y  = int(split_result[0]), int(split_result[1])
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            _paper.append([x, y])
        except:
            if line[0] == 'f':
                line = line.replace('\n', '')
                split_result = line.split(' ')[2].split('=')
                fold_instructions.append((split_result[0], int(split_result[1])))
    paper = []
    for _ in range(max_y + 1):
        row = []
        for _ in range(max_x + 1):
            row.append('.')
        paper.append(row)
        
    for dot in _paper:
        col, row = dot
        paper[row][col] = '#'
            
    return fold_instructions, paper

def do_fold(fold_instruction, paper):
    
    if fold_instruction[0] == 'x':
        # vertical fold
        first_half = [row[:fold_instruction[1]] for row in paper]
        second_half = [row[fold_instruction[1] + 1:] for row in paper]

        for row in range(len(first_half)):
            _col = 0
            for col in range(len(first_half[0]) - 1, -1, -1):
                if first_half[row][col] == '#':
                    second_half[row][_col] = '#'
                _col += 1
            
        paper = second_half
        
        
    elif fold_instruction[0] == 'y':
        # horizontal fold
        first_half = paper[:fold_instruction[1]][:]
        second_half = paper[fold_instruction[1] + 1:][:]
        
        _row = len(second_half) - 1
        for row in range(len(second_half) - 1):
            _col = 0
            for col in range(len(second_half[0])):
                if second_half[_row][_col] == '#':
                    first_half[row][col] = '#'
                _col += 1
            _row -= 1
            
        paper = first_half
        
    return paper

if __name__ == '__main__':
    
    fold_instructions, paper = read_instructions('test_input.txt')
    
    for fold_instruction in fold_instructions:
        paper = do_fold(fold_instruction, paper)
        dots_count = sum(len([c for c in row if c == '#']) for row in paper)
        print(dots_count)
        
    fold_instructions, paper = read_instructions('input.txt')
    
    for fold_instruction in fold_instructions:
        paper = do_fold(fold_instruction, paper)
        dots_count = sum(len([c for c in row if c == '#']) for row in paper)
        print(dots_count)