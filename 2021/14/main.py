def read_input(path):
    
    f = open(path)
    lines = [line.strip().replace('\n', '') for line in f.readlines()]
    f.close()
    
    polymer_template = lines[0]
    
    pair_insertion_rules = {}
    for line in lines[2:]:
        s = [s.strip() for s in line.split('->')]
        pair_insertion_rules[s[0]] = s[1]
        
    return polymer_template, pair_insertion_rules

def get_count(polymer_template, pair_insertion_rules, number_of_steps):
    l = len(polymer_template)
    for step in range(1, number_of_steps + 1):
        t = ''
        for i in range(l - 1):
            pair = polymer_template[i] + polymer_template[i+1]
            to_be_inserted = pair_insertion_rules[pair]
            tmp = pair[0] + to_be_inserted + pair[1]
            t += tmp[:-1]
        t += tmp[-1]
        polymer_template = t
        l = len(polymer_template)
        if step % 10 == 0:
            print(step)
        
    counts = {}
    for c in polymer_template:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            
    d = sorted(counts.items(), key=lambda x: x[1])
    return d[-1][1] - d[0][1]


if __name__ == '__main__':
    
    expected = 1588
    number_of_steps = 10
    polymer_template, pair_insertion_rules = read_input('test_input.txt')
    count = get_count(polymer_template, pair_insertion_rules, number_of_steps)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    expected = 3411
    number_of_steps = 10
    polymer_template, pair_insertion_rules = read_input('input.txt')
    count = get_count(polymer_template, pair_insertion_rules, number_of_steps)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    expected = 2188189693529
    number_of_steps = 40
    polymer_template, pair_insertion_rules = read_input('test_input.txt')
    count = get_count(polymer_template, pair_insertion_rules, number_of_steps)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    number_of_steps = 40
    polymer_template, pair_insertion_rules = read_input('input.txt')
    count = get_count(polymer_template, pair_insertion_rules, number_of_steps)
    print(count)    