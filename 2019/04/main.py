def is_valid(number):
    number = list(str(number))
    two = False
    for i in range(1, len(number)):
        if int(number[i - 1]) > int(number[i]):
            return False
        
        if number[i - 1] == number[i]:
            two = True
        
    return two

def is_valid2(number):
    number = list(str(number))
    
    t = 1
    has_double = False
    for i in range(0, len(number) - 1):
        if int(number[i]) > int(number[i + 1]):
            return False
    
        if number[i] == number[i + 1]:
            t += 1
            
        if number[i] != number[i + 1]:
            if has_double == False and t == 2:
                has_double = True
            t = 1
    
    if t == 2:
        has_double = True
                
    return has_double

def solve():
    count1 = 0
    count2 = 0
    lower = 147981
    upper = 691423
    r = upper - lower
    
    for i in range(r + 1):
        if is_valid(lower + i):
            count1 += 1
        if is_valid2(lower + i):
            count2 += 1
        
    return count1, count2

if __name__ == '__main__':
    
    print(is_valid2(112233))
    print(is_valid2(123444))
    print(is_valid2(111122))
    print(is_valid2(112222))
    
    print(solve())
    