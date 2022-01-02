class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

def get_map(path):
    f = open(path)
    lines = [line.replace('\n', '') for line in f.readlines()]
    f.close()
    return lines

def get_all_paths(map):
    graph = []

if __name__ == '__main__':
    
    test_maps = ['test_input1.txt', 'test_input2.txt', 'test_input3.txt']
    expected = [10, 19, 226]
    
    for test_input, result in zip(test_maps, expected):
        test_map = get_map(test_input)
        count = get_all_paths(test_map)
        if count == result:
            print('ok')
        else:
            print('error')