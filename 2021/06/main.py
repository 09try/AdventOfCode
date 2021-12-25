def lanternfish_aging(lanternfish):
    pass

def run_simulation(initial_state, number_of_days):
    print('running simulation')

    # 2nd approach
    population = {}

    # possible states of lanternfish
    for state in range(9):
        population[str(state)] = 0

    # count of lanternfish in each state
    # in initial population
    for lanternfish in initial_state:
        population[str(lanternfish)] += 1

    # loop through days
    previous_population = population

    for _ in range(number_of_days):
        current_population = {}

        current_population['6'] = previous_population['0']
        current_population['8'] = previous_population['0']

        current_population['7'] = previous_population['8']
        current_population['6'] = current_population['6'] + previous_population['7']
        current_population['5'] = previous_population['6']
        current_population['4'] = previous_population['5']
        current_population['3'] = previous_population['4']
        current_population['2'] = previous_population['3']
        current_population['1'] = previous_population['2']
        current_population['0'] = previous_population['1']

        previous_population = current_population

    my_sum = sum(previous_population.values())
    return my_sum
    # end 2nd approach

    # 1st approach
    for _ in range(number_of_days):
        for i in range(len(initial_state)):
            if initial_state[i] != 0:
                initial_state[i] -= 1
            else:
                initial_state[i] = 6
                initial_state.append(8)
    # end of 1st approach

    return len(initial_state)

if __name__ == '__main__':

    # unit test
    number_of_days = 80
    initial_state = [3, 4, 3, 1, 2]
    lanternfish_count = run_simulation(initial_state, number_of_days)

    if lanternfish_count == 5934:
        print('ok')
    # end of unit test

    # # problem input
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()

    number_of_days = 256
    initial_state = [int(x) for x in lines[0].split(',')]
    lanternfish_count = run_simulation(initial_state, number_of_days)
    print(lanternfish_count)
