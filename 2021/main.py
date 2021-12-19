f = open('input.txt', 'r')
readings = []
for line in f:
    readings.append(int(line))

#print(readings)

previous_reading = -1
increases = 0
for reading in readings:
    current_reading = reading
    if previous_reading != -1:
        if(current_reading > previous_reading):
            increases = increases + 1

    previous_reading = current_reading

print(increases)


first_measurement_window = -1
second_measurement_window = -1
increases = 0
for i  in range(0, len(readings) - 3):
    first_measurement_window = readings[i] + readings[i + 1] + readings[i + 2]
    second_measurement_window = readings[i + 1] + readings[i + 2] + readings[i + 3]

    if(second_measurement_window > first_measurement_window):
        increases = increases + 1

print(increases)