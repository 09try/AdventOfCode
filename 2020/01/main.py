def read_input(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return [int(line) for line in lines]

def get_result2(expense_report):
    for i in range(0, len(expense_report)):
        for j in range(1, len(expense_report)):
            if expense_report[i] + expense_report[j] == 2020:
                return expense_report[i] * expense_report[j]
    return 0

def get_result3(expense_report):
    for i in range(0, len(expense_report)):
        for j in range(1, len(expense_report)):
            for k in range(1, len(expense_report)):
                if expense_report[i] + expense_report[j] + expense_report[k] == 2020:
                    return expense_report[i] * expense_report[j] * expense_report[k]
    return 0
        
if __name__ == '__main__':
    actual = get_result2(read_input('test_input.txt'))
    expected = 514579
    if actual == expected:
        print('ok ', actual)
    else:
        print('error')
        
    actual = get_result2(read_input('input.txt'))
    print(actual)
    
    actual = get_result3(read_input('test_input.txt'))
    expected = 241861950
    if actual == expected:
        print('ok ', actual)
    else:
        print('error')
        
    actual = get_result3(read_input('input.txt'))
    print(actual)