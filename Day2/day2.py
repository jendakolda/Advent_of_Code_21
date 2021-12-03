# Part A:
forward = 0
depth = 0
with open('day2_input.txt', 'r', encoding='utf-8') as movement:
    for line in movement:
        command, value = line.split()
        value = int(value)
        match command:
            case 'up':
                depth -= value
            case 'down':
                depth += value
            case 'forward':
                forward += value
print('Part A:', forward * depth)

# Part B:
forward = 0
depth = 0
aim = 0
with open('day2_input.txt', 'r', encoding='utf-8') as movement:
    for line in movement:
        command, value = line.split()
        value = int(value)
        match command:
            case 'up':
                aim -= value
            case 'down':
                aim += value
            case 'forward':
                forward += value
                depth += aim * value
print('Part B:', forward * depth)
