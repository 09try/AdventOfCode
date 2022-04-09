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

def get_valid_count(passports):
    valid = 0
    for passport in passports:
        if is_valid(passport):
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