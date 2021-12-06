def get_rating(binaries, crit):
    for position in range(len(binaries[0])):
        criterion = most_least_single(binaries, position, function=crit)
        binaries = list(filter(lambda x: str(x[position]) == criterion, binaries))
        if len(binaries) == 1:
            return binlist_to_int(map(str, *binaries))


def binlist_to_int(binlist):
    return int(''.join(binlist), 2)


def most_least_single(binaries, position, function):
    summa = 0
    for i in range(len(binaries)):
        summa += binaries[i][position]
    match function:
        case 'most':
            return str(1) if (summa >= len(binaries) / 2) else str(0)
        case 'least':
            return str(1) if (summa < len(binaries) / 2) else str(0)


def most_least_common(binaries):
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
print('Part B:', get_rating(byte_list, 'most') * get_rating(byte_list, 'least'))


