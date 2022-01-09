import time

# try linked list
# try generator
# try circular linked list - https://realpython.com/linked-lists-python/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for n in nodes:
                node.next = Node(data=n)
                node = node.next
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return ''.join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield None

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

def get_count(polymer_template, pair_insertion_rules, number_of_steps, print_steps=False):
    start_time = time.time()
    
    for step in range(1, number_of_steps + 1):
        if print_steps:
            print('step', step)
        l = len(polymer_template)
        t = ''
        for i in range(l - 1):
            pair = polymer_template[i] + polymer_template[i+1]
            to_be_inserted = pair_insertion_rules[pair]
            tmp = pair[0] + to_be_inserted + pair[1]
            t += tmp[:-1]
        t += tmp[-1]
        polymer_template = t
        
    counts = {}
    for c in polymer_template:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            
    d = sorted(counts.items(), key=lambda x: x[1])
    end_time = time.time()
    diff_time = end_time - start_time
    print('{} get_count seconds'.format(diff_time))
    return d[-1][1] - d[0][1]

def get_count2(polymer_template, pair_insertion_rules, number_of_steps, print_steps=False):
    start_time = time.time()
    
    polymer_template = LinkedList(list(polymer_template))
    
    for step in range(1, number_of_steps + 1):
        if print_steps:
            print('step', step)
        new_polymer_template = LinkedList()
        for n in polymer_template:
            new_polymer_template.add_last(Node(n.data))
            if n.next is not None:
                pair = n.data + n.next.data
                new_node = Node(pair_insertion_rules[pair])
                new_polymer_template.add_last(new_node)
        polymer_template = new_polymer_template
        
    counts = {}
    for n in polymer_template:
        if n.data in counts:
            counts[n.data] += 1
        else:
            counts[n.data] = 1
            
    d = sorted(counts.items(), key=lambda x: x[1])
    end_time = time.time()
    diff_time = end_time - start_time
    print('{} get_count2 seconds'.format(diff_time))
    return d[-1][1] - d[0][1]

def get_count3(polymer_template, pair_insertion_rules, number_of_steps, print_steps=False):
    
    new_pt = []
    pt = polymer_template
    pir = pair_insertion_rules
    
    for step in range(1, number_of_steps + 1):
        if print_steps:
            print('step', step)
            
    counts = {}
    for n in new_pt:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
            
    d = sorted(counts.items(), key=lambda x: x[1])
    end_time = time.time()
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
        
    print('------------------------------------------------------------')
        
    # expected = 1588
    # number_of_steps = 10
    # polymer_template, pair_insertion_rules = read_input('test_input.txt')
    # count = get_count2(polymer_template, pair_insertion_rules, number_of_steps)
    # if count == expected:
    #     print('ok')
    # else:
    #     print('error')
        
    # expected = 3411
    # number_of_steps = 10
    # polymer_template, pair_insertion_rules = read_input('input.txt')
    # count = get_count2(polymer_template, pair_insertion_rules, number_of_steps)
    # if count == expected:
    #     print('ok')
    # else:
    #     print('error')
        
    expected = 2188189693529
    number_of_steps = 40
    polymer_template, pair_insertion_rules = read_input('test_input.txt')
    count = get_count(polymer_template, pair_insertion_rules, number_of_steps, print_steps=False)
    if count == expected:
        print('ok')
    else:
        print('error')
        
    number_of_steps = 40
    polymer_template, pair_insertion_rules = read_input('input.txt')
    count = get_count(polymer_template, pair_insertion_rules, number_of_steps)
    print(count)    