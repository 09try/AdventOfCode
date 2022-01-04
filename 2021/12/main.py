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
            
    def bfs(self, src):
        # mark all the vertices as not visited
        visited = {}
        for key, value in self.vertices.items():
            visited[key] = False
        
        # create a queue for BFS
        queue = []
        
        # mark the source node as visited and enqueue it
        visited[src.name] = True
        queue.append(src)
        
        while queue:
            # dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s.name, end=' ')      
            
            # get all adjacent vertices of the dequeued vertex
            # if adjacent has not been visited, then mark it visited
            # and enqueue it
            for key, value in self.vertices.items():
                if visited[key] == False:
                    queue.append(value)
                    visited[key] = True
                    
    def print_all_paths_from_src_to_dst_util(self, src, dst, visited, path, counter):
        visited[src.name] = True
        path.append(src.name)
        
        if src == dst:
            counter += 1
        else:
            for neighbor in src.neighbors:
                if visited[neighbor] == False:
                    next = self.vertices[neighbor]
                    counter = self.print_all_paths_from_src_to_dst_util(next, dst, visited, path, counter)
                else:
                    if neighbor.isupper():
                        visited[neighbor] = False
                        next = self.vertices[neighbor]
                        counter = self.print_all_paths_from_src_to_dst_util(next, dst, visited, path, counter)
                    else:
                        visited[src.name] = True
        
        path.pop()
        visited[src.name] = False
        return counter
        
    def print_path_from_src_to_dst(self, src, dst):
        
        # mark all the vertices as not visited
        visited = {}
        for key, value in self.vertices.items():
            visited[key] = False
            
        # create an array to store paths
        path = []
        
        counter = 0
        c = self.print_all_paths_from_src_to_dst_util(src, dst, visited, path, counter)
        return c
    
    def print_all_paths_from_src_to_dst_util_part_two(self, src, dst, visited, path, counter, visited_first_time):
        visited[src.name] = True
        path.append(src.name)
        
        if src == dst:
            # if counter == 100 there is twice start
            print(path)
            counter += 1
        else:
            for neighbor in src.neighbors:
                if visited[neighbor] == False:
                    next = self.vertices[neighbor]
                    counter = self.print_all_paths_from_src_to_dst_util_part_two(next, dst, visited, path, counter, visited_first_time)
                else:
                    if neighbor.isupper():
                        visited[neighbor] = False
                        next = self.vertices[neighbor]
                        counter = self.print_all_paths_from_src_to_dst_util_part_two(next, dst, visited, path, counter, visited_first_time)
                    elif visited_first_time == False:
                        visited_first_time = True
                        
                        visited[neighbor] = False
                        next = self.vertices[neighbor]
                        counter = self.print_all_paths_from_src_to_dst_util_part_two(next, dst, visited, path, counter, visited_first_time)
                    else:
                        visited[src.name] = True
        
        path.pop()
        visited[src.name] = False
        return counter
    
    def print_path_from_src_to_dst_part_two(self, src, dst):
        
        # mark all the vertices as not visited
        visited = {}
        for key, value in self.vertices.items():
            visited[key] = False
            
        # create an array to store paths
        path = []
        
        counter = 0
        visited_first_time = False
        c = self.print_all_paths_from_src_to_dst_util_part_two(src, dst, visited, path, counter, visited_first_time)
        return c
        
def get_map(path):
    f = open(path)
    lines = [line.replace('\n', '') for line in f.readlines()]
    f.close()
    return lines

def get_all_paths(map):
    g = Graph()
    
    for line in map:
        p = line.split('-')
        u = Vertex(p[0])
        v = Vertex(p[1])
        g.add_vertex(u)
        g.add_vertex(v)
        g.add_edge(u.name, v.name)
            
    #g.print_graph()
    
    src = g.vertices['start']
    dst = g.vertices['end']
    c = g.print_path_from_src_to_dst(src, dst)
    return c

def get_all_paths_part_two(map):
    g = Graph()
    
    for line in map:
        p = line.split('-')
        u = Vertex(p[0])
        v = Vertex(p[1])
        g.add_vertex(u)
        g.add_vertex(v)
        g.add_edge(u.name, v.name)
            
    #g.print_graph()
    
    src = g.vertices['start']
    dst = g.vertices['end']
    c = g.print_path_from_src_to_dst_part_two(src, dst)
    return c
    
if __name__ == '__main__':
    
    test_maps = ['test_input1.txt', 'test_input2.txt', 'test_input3.txt']
    expected = [10, 19, 226]
    
    for test_input, result in zip(test_maps, expected):
        test_map = get_map(test_input)
        count = get_all_paths(test_map)
        print('expected {} received {}'.format(result, count))
        if count == result:
            print('ok')
        else:
            print('error')
            
    map = get_map('input.txt')
    count = get_all_paths(map)
    print(count)
    if count == 3495:
        print('ok')
    else:
        print('error')
        
        
    # part two
    test_maps = ['test_input1.txt']
    expected = [103]

    #test_maps = ['test_input1.txt', 'test_input2.txt']
    #expected = [103, 3509]

    for test_input, result in zip(test_maps, expected):
        test_map = get_map(test_input)
        count = get_all_paths_part_two(test_map)
        print('expected {} received {}'.format(result, count))
        if count == result:
            print('ok')
        else:
            print('error')