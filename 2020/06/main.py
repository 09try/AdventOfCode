def read_input(path):
    f = open(path, 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def solve(lines):
    
    groups = []
    group = ''
    for line in lines:
        if line != '':
            for c in line:
                if c not in group:
                    group += c
        else:
            if group != '':
                groups.append(group)
                group = ''
    if group != '':
        groups.append(group)
        
    sum_of_counts = sum([len(x) for x in groups])
    
    return sum_of_counts

def solve2(lines):
    answers = {}
    counts = []
    number_of_people_in_group = 0
    counter_of_yes_questions = 0
    
    for line in lines:
        if line != '':
            for question in line:
                if question not in answers:
                    answers[question] = 1
                else:
                    answers[question] += 1
            number_of_people_in_group += 1
        else:
            if number_of_people_in_group == 1:
                counts.append(len(answers))
            else:
                counter_of_yes_questions = 0
                for key, value in answers.items():
                    if value == number_of_people_in_group:
                        counter_of_yes_questions += 1
                counts.append(counter_of_yes_questions)
            answers = {}
            number_of_people_in_group = 0
      
    counter_of_yes_questions = 0
    for key, value in answers.items():
        if value == number_of_people_in_group:
            counter_of_yes_questions += 1
    counts.append(counter_of_yes_questions)
        
    sum_of_counts = sum(counts)
    return sum_of_counts

if __name__ == '__main__':
    lines = read_input('test_input.txt')
    expected = 11
    actual = solve(lines)
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 6630
    actual = solve(lines)
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('test_input.txt')
    expected = 6
    actual = solve2(lines)
    if expected == actual:
        print('ok')
    else:
        print('fail')
        
    lines = read_input('input.txt')
    expected = 3437
    actual = solve2(lines)
    print(actual)
    if expected == actual:
        print('ok')
    else:
        print('fail')