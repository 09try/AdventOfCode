def get_lines(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lines = [line.replace('\n', '') for line in lines]
    return lines

def get_score(lines, score_table):
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
        
    expected = 399153
    lines = get_lines('input.txt')
    score = get_score(lines, score_table)
    if score == expected:
        print('ok')
    else:
        print('error')