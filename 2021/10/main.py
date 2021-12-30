def get_lines(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lines = [line.replace('\n', '') for line in lines]
    return lines

def get_corrupted_lines_score(lines, score_table):
    score = 0

    for line in lines:
        opened_chunks = []
        
        for c in line:
            
            if c == '(':
                opened_chunks.append(c)
            elif c == ')':
                if opened_chunks[-1] != '(':
                    score += score_table[c]
                    break
                else:
                    opened_chunks.pop()
            elif c == '[':
                opened_chunks.append(c)
            elif c == ']':
                if opened_chunks[-1] != '[':
                    score += score_table[c]
                    break
                else:
                    opened_chunks.pop()
            elif c == '{':
                opened_chunks.append(c)
            elif c == '}':
                if opened_chunks[-1] != '{':
                    score += score_table[c]
                    break
                else:
                    opened_chunks.pop()
            elif c == '<':
                opened_chunks.append(c)
            elif c == '>':
                if opened_chunks[-1] != '<':
                    score += score_table[c]
                    break
                else:
                    opened_chunks.pop()
                
    return score

def get_incomplete_lines_score(lines, score_table):

    incomplete_lines = []

    for line in lines:
        opened_chunks = []
        
        is_error_line = False
        
        for c in line:
            
            if c == '(':
                opened_chunks.append(c)
            elif c == ')':
                if opened_chunks[-1] != '(':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            elif c == '[':
                opened_chunks.append(c)
            elif c == ']':
                if opened_chunks[-1] != '[':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            elif c == '{':
                opened_chunks.append(c)
            elif c == '}':
                if opened_chunks[-1] != '{':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            elif c == '<':
                opened_chunks.append(c)
            elif c == '>':
                if opened_chunks[-1] != '<':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
                    
        if is_error_line == False:
            incomplete_lines.append(line)
            
    scores = []
    
    for line in incomplete_lines:
        opened_chunks = []
        
        for c in line:
            
            if c == '(':
                opened_chunks.append(c)
            elif c == ')':
                if opened_chunks[-1] != '(':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            elif c == '[':
                opened_chunks.append(c)
            elif c == ']':
                if opened_chunks[-1] != '[':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            elif c == '{':
                opened_chunks.append(c)
            elif c == '}':
                if opened_chunks[-1] != '{':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            elif c == '<':
                opened_chunks.append(c)
            elif c == '>':
                if opened_chunks[-1] != '<':
                    is_error_line = True
                    break
                else:
                    opened_chunks.pop()
            
        t = []
        for i in range(len(opened_chunks) - 1, -1, -1):
            if opened_chunks[i] == '(':
                t.append(')')

            if opened_chunks[i] == '[':
                t.append(']')

            if opened_chunks[i] == '{':
                t.append('}')

            if opened_chunks[i] == '<':
                t.append('>')
        
        current_score = 0        
        for c in t:
            current_score = current_score * 5 + score_table[c]
        scores.append(current_score)
        
    scores = sorted(scores)
    final_score = 0
    if len(scores) > 1:
        final_score = scores[len(scores) // 2]
    else:
        final_score = scores[0]
                
    return final_score

if __name__ == '__main__':
    
    score_table = {}
    score_table[')'] = 3
    score_table[']'] = 57
    score_table['}'] = 1197
    score_table['>'] = 25137
    
    expected = 26397
    test_lines = get_lines('test_input.txt')
    score = get_corrupted_lines_score(test_lines, score_table)
    if score == expected:
        print('ok')
    else:
        print('error')
        
    expected = 399153
    lines = get_lines('input.txt')
    score = get_corrupted_lines_score(lines, score_table)
    if score == expected:
        print('ok')
    else:
        print('error')
        
        
    score_table = {}
    score_table[')'] = 1
    score_table[']'] = 2
    score_table['}'] = 3
    score_table['>'] = 4
        
    expected = 288957
    score = get_incomplete_lines_score(test_lines, score_table)
    if score == expected:
        print('ok')
    else:
        print('error')
    
    score = get_incomplete_lines_score(lines, score_table)
    print(score)