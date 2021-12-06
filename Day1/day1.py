with open('day1_input.txt', 'r', encoding='utf-8') as log:
    depths = log.readlines()
depth_readings = tuple(int(depth.strip('\n')) for depth in depths)

# Part A:
increases = 0
for i in range(1, len(depth_readings)):
    if depth_readings[i] > depth_readings[i-1]:
        increases += 1
print('Part A: ', increases)

# Part B:
increases_3 = 0
for i in range(3, len(depth_readings)):
    if sum(depth_readings[i-3:i]) > sum(depth_readings[i-4:i-1]):
        increases_3 += 1
print('Part B: ', increases_3)
