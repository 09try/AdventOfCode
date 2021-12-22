f = open('input.txt', 'r')
report = []
for line in f:
    report.append(line.strip())

f.close()

bits = [0 for i in range(len(report[0]))]

for datapoint in report:
    for i in range(0, len(datapoint)):
        if datapoint[i] == '0':
            bits[i] = bits[i] - 1
        elif datapoint[i] == '1':
                bits[i] = bits[i] + 1

#print(bits)

_gamma_rate = [1 if i > 1 else 0 for i in bits]
_epsilon_rate = [0 if i > 1 else 1 for i in bits]

#print(_gamma_rate)
#print(_epsilon_rate)

gamma_rate = 0
for bit in _gamma_rate:
    gamma_rate  = (gamma_rate  << 1) | bit

epsilon_rate = 0
for bit in _epsilon_rate:
    epsilon_rate  = (epsilon_rate  << 1) | bit

#print(gamma_rate)
#print(epsilon_rate)

power_consumption = 0

power_consumption = int(gamma_rate) * int(epsilon_rate)
print(power_consumption)

life_support_rating = 0
oxygen_generator_rating = 0
co2_scrubber_rating = 0


def get_values(input, bit, type):
    zero = 0
    one = 0
    zeros = []
    ones = []
    for datapoint in input:
        if(datapoint[bit] == '0'):
            zero = zero + 1
            zeros.append(datapoint)
        else:
            one = one + 1
            ones.append(datapoint)

    if zero < one:
        if type:
            return ones
        else:
            return zeros
    elif one < zero:
        if type:
            return zeros
        else:
            return ones
    else:
        if type:
            return ones
        else:
            return zeros

report_copy = report
bit = 0

while len(report_copy) != 1:
    report_copy = get_values(report_copy, bit, True)
    bit = bit + 1

oxygen_generator_rating = report_copy[0]

report_copy = report
bit = 0

while len(report_copy) != 1:
    report_copy = get_values(report_copy, bit, False)
    bit = bit + 1

co2_scrubber_rating = report_copy[0]

life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
print(life_support_rating)

