def get_lines(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lines = [line.replace('\n', '') for line in lines]
    return lines

def get_score(lines, score_table):
    score = 0
    
    # chars = {}
    # chars['('] = 0
    # chars[')'] = 0 
    # chars['['] = 0 
    # chars[']'] = 0
    # chars['{'] = 0
    # chars['}'] = 0
    # chars['<'] = 0
    # chars['>'] = 0
    
    # 0 ()
    # 1 []
    # 2 {}
    # 3 <>
    chars = [0, 0, 0, 0]
    previous_char = ''
    
    for line in lines:
        for i, c in enumerate(line):
            
            if c == '(':
                chars[0] += 1
            elif c == ')':
                chars[0] -= 1
            elif c == '[':
                chars[1] += 1
            elif c == ']':
                chars[1] -= 1
            elif c == '{':
                chars[2] += 1
            elif c == '}':
                chars[2] -= 1
            elif c == '<':
                chars[3] += 1
            elif c == '>':
                chars[3] -= 1
                
            previous_char = c

    print()
        
    return score

if __name__ == '__main__':
    
    score_table = {}
    score_table[')'] = 3
    score_table[']'] = 57
    score_table['}'] = 1197
    score_table['>'] = 25137
    
    
    expected = 26397
    lines = get_lines('test_input.txt')
    score = get_score(lines, score_table)
    if score == expected:
        print('ok')
    else:
        print('error')