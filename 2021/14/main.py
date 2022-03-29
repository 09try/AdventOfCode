import time
from collections import Counter
import sys

def read_input(path):
    
    f = open(path)
    lines = [line.strip().replace('\n', '') for line in f.readlines()]
    f.close()
    
    rules = {}
    for line in lines[2:]:
        s = [s.strip() for s in line.split('->')]
        rules[s[0]] = [s[0][0] + s[1], s[1] + s[0][1]]
    
    polymer_template = []
    chars = [c for c in lines[0]]
    for i in range(len(chars) - 1):
        polymer_template.append(chars[i] + chars[i + 1])
    
    return polymer_template, rules

def get_count(polymer_template, rules, number_of_steps):
    start_time = time.time()
    counter = Counter(polymer_template)
    for _ in range(number_of_steps):
        new_counter = {key: 0 for key in rules.keys()}
        for key, value in counter.items():
            new_counter[rules[key][0]] += value
            new_counter[rules[key][1]] += value
            
        counter = new_counter
        
    letters = {}
    for key, value in counter.items():
        if key[0] in letters:
            letters[key[0]] += value
        else:
            letters[key[0]] = value
            
    letters[polymer_template[-1][1]] += 1
    
    min = sys.maxsize
    max = 0
    
    for value in letters.values():
        if value > max:
            max = value
        if value < min:
            min = value
            
    end_time = time.time()
    diff_time = end_time - start_time
    print('get_count elapsed seconds {}'.format(diff_time))
    return max - min


if __name__ == '__main__':
    
    expected = 1588
    number_of_steps = 10
    polymer_template, rules = read_input('test_input.txt')
    count = get_count(polymer_template, rules, number_of_steps)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    expected = 3411
    number_of_steps = 10
    polymer_template, rules = read_input('input.txt')
    count = get_count(polymer_template, rules, number_of_steps)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    print('------------------------------------------------------------')
        
    expected = 2188189693529
    number_of_steps = 40
    polymer_template, rules = read_input('test_input.txt')
    count = get_count(polymer_template, rules, number_of_steps)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    number_of_steps = 40
    polymer_template, rules = read_input('input.txt')
    count = get_count(polymer_template, rules, number_of_steps)
    print(count)