# number - number of segments
# 0 - 6
# 1 - 2
# 2 - 5
# 3 - 5
# 4 - 4
# 5 - 5
# 6 - 6
# 7 - 3
# 8 - 7
# 9 - 6

# number - segments
# 1, 4, 7, 8
# 1 - cf
# 4 - bcdf
# 7 - acf
# 8 - abcdefg

if __name__ == '__main__':
    
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    
    count = 0
    for line in lines:
        digits = line.split('|')[1].split(' ')
        
        for digit in digits:
            
            digit = digit.replace('\n', '')
            
            if len(digit) == 2:
                count += 1
            elif len(digit) == 4:
                count += 1
            elif len(digit) == 3:
                count += 1
            elif len(digit) == 7:
                count += 1
                
    print(count)
    
    
    #  aaaa
    # b    c
    # b    c
    #  dddd
    # e    f 
    # e    f
    #  gggg
    
    for line in lines:
        # get input values and output values        
        first_part, second_part = line.replace('\n', '').split('|')
        
        # get digits in the input values
        first_part_digits = first_part.split(' ')
        
        display = {}
        # 0
        display['abcefg'] = ''
        # 1
        display['cf'] = ''
        # 2
        display['acdeg'] = ''
        # 3
        display['acdfg'] = ''
        # 4
        display['bcdf'] = ''
        # 5
        display['abdfg'] = ''
        # 6
        display['abdefg'] = ''
        # 7
        display['acf'] = ''
        # 8
        display['abcdefg'] = ''
        # 9
        display['abcdfg'] = ''
        
        tmp = first_part_digits
    
        # loop through digits until all are decoded        
        counter = 0
        while tmp != []:
            
            digit = tmp[counter]
            
            if len(digit) == 2:
                # number one
                tmp.remove(digit)
                display['cf'] = digit
            elif len(digit) == 4:
                # number four
                tmp.remove(digit)
                display['bcdf'] = digit
            elif len(digit) == 3:
                # number seven
                tmp.remove(digit)
                display['acf'] = digit
            elif len(digit) == 7:
                # number eight
                tmp.remove(digit)
                display['abcdfg'] = digit
            
            if counter == len(tmp) - 1:
                counter = 0
                
            counter += 1
            
        # decode output values
        
        # get sum
            
        
    