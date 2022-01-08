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

if __name__ == '__main__':
    
    expected = 1588
    polymer_template, pair_insertion_rules = read_input('test_input.txt')
    
    for step in range(10):
        t = ''
        for i in range(len(polymer_template) - 1):
            pair = polymer_template[i] + polymer_template[i+1]
            to_be_inserted = pair_insertion_rules[pair]
            t += pair[0] + to_be_inserted
    
    