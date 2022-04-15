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
    
    ok_field_count = 0
    
    for _split_result in split_result:
        s = _split_result.split(':')
        
        if s[0] == 'byr':
            n = int(s[1])
            if len(str(n)) == 4 and n >= 1920 and n <= 2002:
                ok_field_count += 1
        if s[0] == 'iyr':
            n = int(s[1])
            if len(str(n)) == 4 and n >= 2010 and n <= 2020:
                ok_field_count += 1
        if s[0] == 'eyr':
            n = int(s[1])
            if len(str(n)) == 4 and n >= 2020 and n <= 2030:
                ok_field_count += 1
        if s[0] == fields[3]:
            unit = s[1][-2:]
            if unit == 'cm' or unit == 'in':
                value = int(s[1][:-2])
                if unit == 'cm':
                    if value >= 150 and value <= 193:
                        ok_field_count += 1
                if unit == 'in':
                    if value >= 59 and value <= 76:
                        ok_field_count += 1
        if s[0] == 'hcl':
            v = s[1][1:]
            if s[1][0] == '#' and len(v) == 6:
                tmp = 0
                for c in v:
                    if c in '0123456789abcdef':
                        tmp += 1
                if tmp == len(v):
                    ok_field_count += 1
        if s[0] == fields[5]:
            allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if s[1] in allowed:
                ok_field_count += 1
        if s[0] == fields[6]:
            if len(s[1]) == 9:
                tmp = 0
                for c in s[1]:
                    if c in '0123456789':
                        tmp += 1
                if tmp == len(s[1]):
                    ok_field_count += 1
        if s[0] == fields[7]:
            pass
    
    if ok_field_count == 7:
        return True
    else:
        return False

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