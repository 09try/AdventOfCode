f = open('input.txt', 'r')
report = []
for line in f:
    report.append(line.strip())

f.close()

print(report)

power_consumption = 0
gamma_rate = 0b0
epsilon_rate = 0b0

power_consumption = int(gamma_rate) * int(epsilon_rate)
print(power_consumption)