import numpy as np
from scipy.optimize import minimize_scalar


def objective_function_A(depth, coords):
    return sum([abs(i - depth) for i in coords])


def objective_function_B(depth: int, coords: list):
    return sum([sum(range(1, abs(i - round(depth)) + 1)) for i in coords])


with open('day7_input.txt', 'r', encoding='utf-8') as f:
    crab_coords = list(map(int, f.read().split(',')))

res_A = minimize_scalar(objective_function_A, args=crab_coords)
print('Part A:', int(res_A["fun"]))
res_B = minimize_scalar(objective_function_B, args=crab_coords)
print('Part B:', int(res_B["fun"]))





