import timeit

with open('day6_input.txt', 'r', encoding='utf-8') as f:
    fish = list(map(int, f.read().split(',')))

print(fish)
for step in range(256):
    start = timeit.default_timer()

    new = 0
    for num, f in enumerate(fish):
        if f == 0:
            fish[num] = 6
            fish.append(9)
        else:
            fish[num] = f - 1
    stop = timeit.default_timer()
    print(step, 'Time:', stop - start)

print('Part A:', len(fish))
