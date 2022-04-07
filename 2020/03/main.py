def read_map(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return [[c for c in line.strip()] for line in lines]
    
def count_trees(my_map):
    tree = '#'
    row = 1
    col = 0
    height = len(my_map)
    width = len(my_map[0])
    tree_count = 0
    while row != height:
        col += 3
        col %= width
        
        if my_map[row][col] == tree:
            tree_count += 1
        
        row += 1
        
    return tree_count

def count_trees2(my_map, right, down):
    tree = '#'
    row = down
    col = 0
    height = len(my_map)
    width = len(my_map[0])
    tree_count = 0
    while row < height:
        col += right
        col %= width
        
        if my_map[row][col] == tree:
            tree_count += 1
        
        row += down
        
    return tree_count
    
if __name__ == '__main__':
    expected = 7
    actual = count_trees(read_map('test_input.txt'))
    if expected == actual:
        print('ok')
    else:
        print('fail')

    expected = 220
    actual = count_trees(read_map('input.txt'))
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    expected = 336
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    actual = 1
    for r, d in zip(right, down):
        actual *= count_trees2(read_map('test_input.txt'), r, d)
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    actual = 1
    for r, d in zip(right, down):
        actual *= count_trees2(read_map('input.txt'), r, d)
    print(actual)