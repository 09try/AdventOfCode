def read_input(path):
    f = open(path, 'r')
    lines = f.readlines()
    
    passports = []
    passport = []
    for line in lines:
        if line != '\n':
            passport.append(line.strip())
        else:
            if passport != []:
                passports.append(' '.join(passport))
                passport = []
                
    if passport != []:
        passports.append(' '.join(passport))
    
    return passports

def is_valid(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for field in fields:
        if field not in passport:
            if field == 'cid':
                pass
            else:
                return False
    
    return True

def is_valid2(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for field in fields:
        if field not in passport:
            if field == 'cid':
                pass
            else:
                return False
    
    split_result = passport.split(' ')
    
    for _split_result in split_result:
        s = _split_result.split(':')
        
        if s[0] == fields[0]:
            n = int(s[1])
            if len(str(n)) != 4:
                return False
            if n < 1920 or n > 2002:
                return False
        elif s[0] == fields[1]:
            n = int(s[1])
            if len(str(n)) != 4:
                return False
            if n < 2010 or n > 2020:
                return False
        elif s[0] == fields[2]:
            n = int(s[1])
            if len(str(n)) != 4:
                return False
            if n < 2020 or n > 2030:
                return False
        elif s[0] == fields[3]:
            unit = s[1][-2:]
            if unit != 'cm' and unit != 'in':
                return False
            value = int(s[1][:-2])
            if unit == 'cm':
                if value < 150 and value > 193:
                    return False
            if unit == 'in':
                if value < 59 and value > 76:
                    return False
        elif s[0] == fields[4]:
            v = s[1][1:]
            if len(v) != 6:
                return False
            for c in v:
                if c not in '0123456789abcdef':
                    return False
        elif s[0] == fields[5]:
            allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if s[1] not in allowed:
                return False
        elif s[0] == fields[6]:
            if len(s[1]) != 9:
                return False
        elif s[0] == fields[7]:
            pass
    
    return True

def get_valid_count(passports):
    valid = 0
    for passport in passports:
        if is_valid(passport):
            valid += 1
            
    return valid

def get_valid_count2(passports):
    valid = 0
    for passport in passports:
        if is_valid2(passport):
            valid += 1
            
    return valid
    
if __name__ == '__main__':

    expected = 2
    passports = read_input('test_input.txt')
    actual = get_valid_count(passports)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
       
    expected = 264 
    passports = read_input('input.txt')
    actual = get_valid_count(passports)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
    
    expected = 4
    passports = read_input('test_input2.txt')
    actual = get_valid_count2(passports)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    expected = 0
    passports = read_input('test_input3.txt')
    actual = get_valid_count2(passports)
    
    if expected == actual:
        print('ok')
    else:
        print('fail')
    
    passports = read_input('input.txt')
    actual = get_valid_count2(passports)
    print(actual)