import numpy as np


def check_lower(x, y, h, v):
    return heights[x, y] < heights[x + h, y + v]


def check_lowest(row, col):

    lower_surrounding = []
    for k, l in indices:
        if (row + k in range(rows)) and (col + l in range(cols)):
            lower_surrounding.append(check_lower(row, col, k, l))
    return all(lower_surrounding)


indices = [(-1, 0), (0, -1), (0, 1), (1, 0)]
height_list = []
with open('day9_input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        height_list.append([int(i) for i in line.strip('\n')])

heights = np.array(height_list)
rows, cols = heights.shape

low_indices = []
for i in range(rows):
    for j in range(cols):
        if check_lowest(i, j):
            low_indices.append([i, j])

print('Part A:', sum([heights[i, j] + 1 for i, j in low_indices]))




