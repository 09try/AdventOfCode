from os import error

def read_instructions(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    
    fold_instructions, dots = [], []
    max_x, max_y = 0, 0
    for line in lines:
        if line.startswith('f'):
            line = line.replace('\n', '')
            split_result = line.split(' ')[2].split('=')
            fold_instructions.append((split_result[0], int(split_result[1])))
        else:
            split_result = line.replace('\n', '').split(',')
            if len(split_result) > 1:
                x, y  = int(split_result[0]), int(split_result[1])
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                dots.append([x, y])
        
    paper = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        
    for dot in dots:
        col, row = dot
        paper[row][col] = '#'
        
    return fold_instructions, paper

def fold_paper(fold_instruction, paper):
    output  = []
    if fold_instruction[0] == 'x':
        x = fold_instruction[1]
        
        left = [r[:x] for r in paper]
        right = [r[x+1:][::-1] for r in paper]
        
        even_out = 0
        if len(left[0]) != len(right[0]):
            print('uneven vertical split')
            even_out = 1
            
        for r in range(len(left)):
            for c in range(len(left[r]) - even_out):
                if right[r][c] == '#':
                    _c = c + even_out
                    left[r][_c] = '#'
                    
        output = left
        
    elif fold_instruction[0] == 'y':
        y = fold_instruction[1]
        
        top = paper[:y]
        bottom = paper[y+1:][::-1]
        
        even_out = 0
        if len(top) != len(bottom):
            print('uneven horizontal split')
            even_out = len(top) - len(bottom)
            
        for r in range(len(top) - even_out):
            for c in range(len(top[r])):
                if bottom[r][c] == '#':
                    top[r + even_out][c] = '#'
                    
        output = top
        
    return output
        

def do_fold(fold_instruction, paper):
    
    if fold_instruction[0] == 'x':
        # vertical fold
        x = fold_instruction[1]
        
        first_half = [row[:x] for row in paper]
        second_half = [row[(x + 1):] for row in paper]
        
        r = len(first_half)
        c = len(first_half[0])
     
        for row in range(r):
            _col = 0
            for col in range(c - 1, -1, -1):
                if first_half[row][col] == '#':
                    try:
                        second_half[row][_col] = '#'
                    except:
                        print(error)
                _col += 1

        paper = second_half
        
    elif fold_instruction[0] == 'y':
        # horizontal fold
        
        y = fold_instruction[1]
        
        first_half = paper[:y][:]
        second_half = paper[y + 1:][:]
        
        first_half = paper[:y]
        second_half = paper[y + 1:][::-1]
        
        if len(first_half[0]) > len(second_half[0]):
            print('handle uneven fold 1')

        if len(first_half[0]) < len(second_half[0]):
            print('handle uneven fold 2')
        
        _row = len(second_half) - 1
        for row in range(len(second_half)):
            _col = 0
            for col in range(len(second_half[0])):
                if second_half[_row][_col] == '#':
                    first_half[row][col] = '#'
                _col += 1
            _row -= 1
            
        paper = first_half
        
    return paper

def do_fold2(fold_instruction, paper):
    
    output = []
    
    if fold_instruction[0] == 'x':
        # vertical
        col = fold_instruction[1]
    
        first_half = []
        second_half = []
        
        for i in range(len(paper)):
            row_first_half = []
            row_second_half = []
            for j in range(len(paper[i])):
                if j < col:
                    row_first_half.append(paper[i][j])
                if j > col:
                    row_second_half.append(paper[i][j])
                
            first_half.append(row_first_half)
            second_half.append(row_second_half)
            
        if len(first_half) != len(second_half):
            print()
            
        if len(first_half[0]) != len(second_half[0]):
            print
            
        # fold left
        for i in range(len(second_half)):
            second_half[i].reverse()
            
        for i in range(len(second_half)):
            for j in range(len(second_half[i])):
                if first_half[i][j] == '#':
                    second_half[i][j] = '#'
                    
        output = second_half
    
    elif fold_instruction[0] == 'y':
        # horizontal
        row = fold_instruction[1]
        
        first_half = paper[:row][:]
        second_half = paper[1 + row:][:]
        
        _second_half_tmp = []
        
        for i in range(len(second_half) - 1, -1, -1):
            r = second_half[i]
            _second_half_tmp.append(r)
        
        for i in range(len(first_half)):
            for j in range(len(first_half[i])):
                if _second_half_tmp[i][j] == '#':
                    first_half[i][j] = '#'
                    
        output = first_half
        
    return output

if __name__ == '__main__':
    
    paper = []
    fold_instructions, paper = read_instructions('test_input.txt')
    first_expected = 17
    for i, fold_instruction in enumerate(fold_instructions):
        paper = fold_paper(fold_instruction, paper)
        dots_count = sum(len([c for c in row if c == '#']) for row in paper)
        if i == 0:
            if dots_count == first_expected:
                print('ok')
            else:
                print('error')
        #print(dots_count)
        
    paper = []
    fold_instructions, paper = read_instructions('input.txt')
    first_expected = 602
    for i, fold_instruction in enumerate(fold_instructions):
        paper = fold_paper(fold_instruction, paper)
        dots_count = sum(len([c for c in row if c == '#']) for row in paper)
        if i == 0:
            if dots_count == first_expected:
                print('ok')
            else:
                print('error')
        #print(dots_count)
        
    for row in range(len(paper)):
        for col in range(len(paper[row])):
            print(paper[row][col], end=' ')
        print()