def read_list(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines
    
def get_valid_count(lines):
    output = 0
    
    for line in lines:
        split_result = line.split(' ')
        lowest, highest = split_result[0].split('-')
        lowest = int(lowest)
        highest = int(highest)
        
        letter = split_result[1][0]
        
        password = split_result[2]
        
        d = {}
        for c in password:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        if letter in d:
            if d[letter] >= lowest and d[letter] <= highest:
                output += 1 
        
    return output

def get_valid_count2(lines):
    output = 0
    
    for line in lines:
        split_result = line.split(' ')
        first, second = split_result[0].split('-')
        first = int(first)
        second = int(second)
        
        letter = split_result[1][0]
        
        password = split_result[2]
        
        if password[first - 1] == letter and password[second - 1] != letter:
            output += 1
            
        if password[first - 1] != letter and password[second - 1] == letter:
            output += 1
        
        
    return output
    
if __name__ == '__main__':

    expected = 2
    actual = get_valid_count(read_list('test_input.txt'))
    if expected == actual:
        print('ok')
    else:
        print('error')
    
    expected = 564
    actual = get_valid_count(read_list('input.txt'))
    if expected == actual:
        print('ok')
    else:
        print('error')
        
    print(get_valid_count2(read_list('input.txt')))