class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
            
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
        
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
        
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
        

def get_map(path):
    f = open(path)
    lines = [line.replace('\n', '') for line in f.readlines()]
    f.close()
    return lines

def get_all_paths(map):
    g = Graph()
    
    for line in map:
        p = line.split('-')
        g.add_vertex(Vertex(p[0]))
        g.add_vertex(Vertex(p[1]))
        g.add_edge(p[0], p[1])
            
    g.print_graph()
    
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
            
        print()
        print()