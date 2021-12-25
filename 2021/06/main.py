def run_simulation(initial_state, number_of_days):
    print('running simulation')
    for day in range(number_of_days):
        for i in range(len(initial_state)):
            if initial_state[i] != 0:
                initial_state[i] -= 1
            else:
                initial_state[i] = 6
                initial_state.append(8)

        #print('day', day)

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
