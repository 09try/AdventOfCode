from collections import defaultdict
  
# This class represents a directed graph
# using adjacency list representation
class Graph:
  
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
         
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):
 
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            #print (path)
            pass
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        # Mark all the vertices as not visited
        visited = {}
        for key, value in self.graph.items():
            visited[key] = False
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


class Node():
    def __init__(self, coordinate, weight):
        self.coordinate = coordinate
        self.weight = weight

def read_input(path):
    f = open(path, 'r')
    lines = [line.strip().replace('\n', '') for line in f.readlines()]
    f.close()
    
    return [[int(risk_level) for risk_level in line] for line in lines]
    
all_paths = [[]]    

def get_optimal_path_risk_level(cavern):
    
    graph = {}
    neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    g = Graph(len(cavern) * len(cavern[0]))

    for row in range(len(cavern)):
        for col in range(len(cavern[0])):
            l = []
            for neighbor in neighbors:
                if row + neighbor[0] >= 0 and row + neighbor[0] < len(cavern):
                    if col + neighbor[1] >= 0 and col + neighbor[1] < len(cavern[0]):
                        _row = row + neighbor[0]
                        _col = col + neighbor[1]
                        node = Node('{},{}'.format(_row, _col), cavern[_row][_col])
                        l.append('{},{}'.format(_row, _col))
                        g.addEdge('{},{}'.format(row, col), '{},{}'.format(_row, _col))
            graph['{},{}'.format(row, col)] = l
    
    l = BFS_SP(graph, '0,0', '9,9')
    print(l)
    
    s = '0,0'
    e = '9,9'
    
    g.printAllPaths(s, e)
        
    # depth_first(graph, '0,0', [])
    
    print(all_paths)
    
def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return new_path
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return []
    
if __name__ == '__main__':
    
    cavern = read_input('test_input.txt')
    expected = 40
    total_risk = get_optimal_path_risk_level(cavern)
    
    if total_risk == expected:
        print('ok')
    else:
        print('fail')