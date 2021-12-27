# number - segments
# 1, 4, 7, 8
# 1 - cf
# 4 - bcdf
# 7 - acf
# 8 - abcdefg

#  aaaa
# b    c
# b    c
#  dddd
# e    f 
# e    f
#  gggg

def create_mapping(first_part):
    
    # initial mapping
    current_mapping = {}
    # 'abcefg': 0
    # 'cf': 1
    # 'acdeg': 2
    # 'acdfg': 3
    # 'bcdf': 4
    # 'abdfg': 5
    # 'abdefg': 6
    # 'acf': 7
    # 'abcdefg': 8
    # 'abcdfg': 9
    # mapping['a'] = 0
    # mapping['b'] = 1
    # mapping['c'] = 2
    # mapping['d'] = 3
    # mapping['e'] = 4
    # mapping['f'] = 5
    # mapping['g'] = 6
    current_mapping[0] = 'a'
    current_mapping[1] = 'b'
    current_mapping[2] = 'c'
    current_mapping[3] = 'd'
    current_mapping[4] = 'e'
    current_mapping[5] = 'f'
    current_mapping[6] = 'g'
    
    already_replaced_chars = {}
    new_mapping = {}
    
    first_part_digits = first_part.split(' ')
    
    first_part_digits = sorted(first_part_digits, key=len)
    
    four = ''
    seven = ''
    one = ''
    
    # rewrite for loop to while loop to get last two indexes of mapping
    for digit in first_part_digits:
        
        digit = sorted(digit)
        
        if len(digit) == 2:
            # number 1
            already_replaced_chars[2] = current_mapping[2]
            already_replaced_chars[5] = current_mapping[5]
            new_mapping[2] = digit[0]
            new_mapping[5] = digit[1]
            one = digit
        elif len(digit) == 3:
            # number 7
            already_replaced_chars[6] = current_mapping[6]
            new_mapping[0] = digit[2]
            seven = digit
        elif len(digit) == 4:
            # number 4
            already_replaced_chars[1] = current_mapping[1]
            already_replaced_chars[3] = current_mapping[3]
            new_mapping[1] = digit[0]
            new_mapping[3] = digit[3]
            four = digit
        elif len(digit) == 5:
            # number 2, 3, 5
            pass
        elif len(digit) == 6:
            # number 0, 6, 9
            
            chars_from_one = 0
            
            # number 9 is the same as 4 + 7 + one char which is not in 4 and 7
            target = ''
            index = 0
            for i, c in enumerate(digit):
                if c in four or c in seven:
                    pass
                else:
                    target = c
                    index = i
                    
                # number six doesnt have one char from number one
                if c in one:
                    chars_from_one += 1
            
            # number nine   
            if target != '':
                new_mapping[6] = digit[index]
            # end of number nine
            
            # number six
            if chars_from_one != 2:
                print()
                new_mapping[4] = digit[2]
                
            # end of number six
            
            
        elif len(digit) == 7:
            # number 8 is not helpful
            pass
        
    return new_mapping

def get_displayed_number(segments, mapping):
    segments = ''.join(sorted(segments))
    
    #          a      b      c      d      e      f      g  
    bools = [False, False, False, False, False, False, False]
    zero = [True, True, True, False, True, True, True]
    one = [False, False, True, False, False, True, False]
    two = [True, False, True, True, True, False, True]
    three = [True, False, True, True, False, True, True]
    four = [False, True, True, True, False, True, False]
    five = [True, True, False, True, False, True, True]
    six = [True, True, False, True, True, True, True]
    seven = [True, False, True, False, False, True, False]
    eight = [True, True, True, True, True, True, True]
    nine = [True, True, True, True, False, True, True]
    
    output = [False, False, False, False, False, False, False]
    for segment in segments:
        # rewrite according to new mapping
        for index, char in mapping.items():
            if char == segment:
                output[index] = True
    
    if output == zero:
        return '0'
    elif output == one:
        return '1'
    elif output == two:
        return '2'
    elif output == three:
        return '3'
    elif output == four:
        return '4'
    elif output == five:
        return '5'
    elif output == six:
        return '6'
    elif output == seven:
        return '7'
    elif output == eight:
        return '8'
    elif output == nine:
        return '9'
    

if __name__ == '__main__':
    
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    
    expected = 352
    
    count = 0
    for line in lines:
        digits = line.split('|')[1].split(' ')
        
        for digit in digits:
            digit = digit.replace('\n', '')
            
            if len(digit) == 2:
                # number one
                count += 1
            elif len(digit) == 4:
                # number four
                count += 1
            elif len(digit) == 3:
                # number seven
                count += 1
            elif len(digit) == 7:
                # number eight
                count += 1

    print(count)
    if count != expected:
        print('error')
    
    total_sum = 0
    for line in lines:
        
        # get input values and output values        
        first_part, second_part = line.replace('\n', '').split('|')
        
        # create mapping from the first part
        mapping = create_mapping(first_part)
            
        # gut number for the sum from the second part
        line_sum = ''
        second_part = second_part.split(' ')
        for digit in second_part:
            if digit != '':
                num = get_displayed_number(digit, mapping)
                if num != None:
                    line_sum += num
                else:
                    print('error')
            
        total_sum += int(line_sum)
        
    print(total_sum)
        
            
        
    