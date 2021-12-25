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