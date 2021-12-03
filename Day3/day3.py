from collections import deque


def get_rating(binaries, crit):
    for position in range(len(binaries[0])):
        criterion = most_least_single(binaries, position, function=crit)
        filtered = list(filter(lambda x: x[position] == criterion, binaries))
        binaries = filtered[1:]
        if len(binaries) == 1:
            return binlist_to_int(binaries)


def get_scrubber():
    pass


def binlist_to_int(binlist):
    return int(''.join(binlist), 2)


def most_least_single(binaries, position, function):
    summa = 0
    for i in range(len(binaries)):
        summa += binaries[i][position]


        match function:
            case 'most':
                return binlist_to_int([str(1) if i > len(binaries) / 2 else str(0) for i in summas])
            case 'least':
                return binlist_to_int([str(1) if i <= len(binaries) / 2 else str(0) for i in summas])


def most_least_common(binaries, positions=None, function='both'):
    summas = list()
    for j in range(len(binaries[0])):
        counter = 0
        for i in range(len(binaries)):
            counter += binaries[i][j]
        summas.append(counter)
        most = binlist_to_int([str(1) if i > len(binaries) / 2 else str(0) for i in summas])
        least = binlist_to_int([str(1) if i <= len(binaries) / 2 else str(0) for i in summas])
        return most, least


with open('day3_input.txt', 'r', encoding='utf-8') as readings:
    byte_list = list()
    for line in readings:
        byte_list.append(tuple(int(i) for i in line.strip('\n')))

# Part A:
gamma, epsilon = most_least_common(byte_list)
print('Part A:', gamma * epsilon)

# Part B:
# oxygen == most
# print('Part B:', get_rating(byte_list, 'most'))

# least_bit = most_least_common(byte_list, 1, function='least')
# filtered_least = list(filter(lambda x: x[0] == least_bit, byte_list))
# print(len(filtered_most), len(filtered_least))

