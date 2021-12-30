def get_lines(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lines = [line.replace('\n', '') for line in lines]
    return lines

def get_score(lines, score_table):
    score = 0

    error_chars = []

    for line_number, line in enumerate(lines):
        
        opened_chunks = []
        
        for i, c in enumerate(line):
            
            if c == '(':
                opened_chunks.append(c)
            elif c == ')':
                if opened_chunks[-1] != '(':
                    print('wrong c', i, line_number)
                    error_chars.append(c)
                    break
                else:
                    opened_chunks.pop()
            elif c == '[':
                opened_chunks.append(c)
            elif c == ']':
                if opened_chunks[-1] != '[':
                    print('wrong c', i, line_number)
                    error_chars.append(c)
                    break
                else:
                    opened_chunks.pop()
            elif c == '{':
                opened_chunks.append(c)
            elif c == '}':
                if opened_chunks[-1] != '{':
                    print('wrong c', i, line_number)
                    error_chars.append(c)
                    break
                else:
                    opened_chunks.pop()
            elif c == '<':
                opened_chunks.append(c)
            elif c == '>':
                if opened_chunks[-1] != '<':
                    print('wrong c', i, line_number)
                    error_chars.append(c)
                    break
                else:
                    opened_chunks.pop()
                
            previous_char = c
        
    score = sum([score_table[s] for s in error_chars])
        
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
        
    lines = get_lines('input.txt')
    score = get_score(lines, score_table)
    print(score)