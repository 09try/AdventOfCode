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
    current_mapping[0] = 'a'
    current_mapping[1] = 'b'
    current_mapping[2] = 'c'
    current_mapping[3] = 'd'
    current_mapping[4] = 'e'
    current_mapping[5] = 'f'
    current_mapping[6] = 'g'
    
    new_mapping = {}
    
    first_part_digits = first_part.split(' ')
    first_part_digits = sorted(first_part_digits, key=len)

    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    
    # rewrite for loop to while loop to get last two indexes of mapping
    for digit in first_part_digits:
        
        digit = sorted(digit)
        
        if len(digit) == 2:
            # number 1
            # possible error - maybe switch index 2 and index 5 later when chars for number 2 and 5 are known
            new_mapping[2] = digit[0]
            new_mapping[5] = digit[1]
            one = digit
        elif len(digit) == 3:
            # number 7
            for d in digit:
                if d not in one:
                    new_mapping[0] = d
            seven = digit
        elif len(digit) == 4:
            # number 4
            # possible error - maybe switch index 1 and index 3 later when chars for number 3 are known
            for d in digit:
                if d not in new_mapping.values():
                    new_mapping[1] = d
                    break

            for d in digit:
                if d not in new_mapping.values():
                    new_mapping[3] = d
                    break
                
            four = digit
        elif len(digit) == 5:
            # number 2, 3, 5

            # number 3 has all chars from number 1
            # numbers 2 and 5 don't have one char from number 1
            chars_occuring_in_1_counter = 0
            chars_occuring_in_4_counter = 0
            
            target = ''
            for c in digit:
                if c in one:
                    chars_occuring_in_1_counter += 1
                    
                if c in four:
                    chars_occuring_in_4_counter += 1
                    
            # it is number 3 if True    
            if chars_occuring_in_1_counter == 2:
                three = digit
                
                # correction of number 4 chars
                for c in four:
                    if c not in three:
                        new_mapping[1] = c
                        
                    if c in three and c not in one:
                        new_mapping[3] = c
                         
            # number 5 has three same chars as number 4
            if chars_occuring_in_4_counter == 3 and chars_occuring_in_1_counter == 1:
                five = digit
                
            # number 2 has two chars in common with number 4 and one char with number 1
            if chars_occuring_in_4_counter == 2 and chars_occuring_in_1_counter == 1:
                two = digit
                
            # correction of number 1 chars
            if two != '' and five != '':
                for c in one:
                    if c in two:
                        new_mapping[2] = c
                        
                    if c in five:
                        new_mapping[5] = c
            
        elif len(digit) == 6:
            # number 0, 6, 9
            
            chars_occuring_in_1_counter = 0
            
            # number 9 is the same as 4 + 7 + one char which is not in 4 and 7
            target = ''
            for c in digit:
                if c not in four and c not in seven:
                    target = c
                    
                # number six doesn't have one char from number one
                if c in one:
                    chars_occuring_in_1_counter += 1
            
            # number nine   
            if target != '' and nine == '':
                new_mapping[6] = target
                nine = digit
            
            # number six
            if chars_occuring_in_1_counter != 2:
                #new_mapping[4] = digit[2]
                
                for d in digit:
                    if d not in new_mapping.values():
                        new_mapping[4] = d
                        break
                six = digit
                
            # number zero
            
            
        elif len(digit) == 7:
            # number 8 is not helpful
            eight = digit
        
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
                break
    
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
    if count == expected:
        print('ok')
    else:
        print('error')
        
        
    line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    expected = 5353
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
    
    if int(line_sum) == expected:
        print('ok')
    else:
        print('error')
        
    
    # total_sum = 0
    # for line in lines:
        
    #     # get input values and output values
    #     first_part, second_part = line.replace('\n', '').split('|')
        
    #     # create mapping from the first part
    #     mapping = create_mapping(first_part)
            
    #     # gut number for the sum from the second part
    #     line_sum = ''
    #     second_part = second_part.split(' ')
    #     for digit in second_part:
    #         if digit != '':
    #             num = get_displayed_number(digit, mapping)
    #             if num != None:
    #                 line_sum += num
    #             else:
    #                 print('error')
            
    #     total_sum += int(line_sum)
        
    # print(total_sum)
        