def get_cheapest_position(horizontal_positions):
    min_position = min(horizontal_positions)
    max_position = max(horizontal_positions)

    costs = dict()
    for position_to_align_to in range(min_position, max_position + 1):
        
        current_cost = 0
        
        for position in horizontal_positions:
            current_cost += abs(position - position_to_align_to)
            
        costs[position_to_align_to] = current_cost
        
    cheapest_position = min(costs, key=costs.get)
    fuel = costs[cheapest_position]
    
    return fuel

def get_cheapest_position_v2(horizontal_positions):
    min_position = min(horizontal_positions)
    max_position = max(horizontal_positions)

    costs = dict()
    for position_to_align_to in range(min_position, max_position + 1):
        
        current_cost = 0
        
        for position in horizontal_positions:
            diff = abs(position - position_to_align_to)
            
            t = sum([x for x in range(diff + 1)])
            
            current_cost += t
            
        costs[position_to_align_to] = current_cost
        
    cheapest_position = min(costs, key=costs.get)
    fuel = costs[cheapest_position]
    
    return fuel

if __name__ == '__main__':
    horizontal_positions_test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    expected_result = 37
    if get_cheapest_position(horizontal_positions_test) == expected_result:
        print('ok')
    else:
        print('nok')    
        
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    
    horizontal_positions = [int(x) for x in lines[0].split(',')]
    print(get_cheapest_position(horizontal_positions))
    
    expected_result = 168
    if get_cheapest_position_v2(horizontal_positions_test) == expected_result:
        print('ok')
    else:
        print('nok')    
        
    print(get_cheapest_position_v2(horizontal_positions))
    
    