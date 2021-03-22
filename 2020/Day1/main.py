from functools import reduce
from itertools import combinations

SUM_VALUE = 2020

with open("input") as f:
    input_data = [int(val) for val in f.read().split("\n")]


def get_multiplication(sum_value: int, numbers_of_sum: int):
    try:
        combination = [
            comb
            for comb in combinations(input_data, numbers_of_sum)
            if sum(comb) == sum_value
        ][0]
        return reduce((lambda x, y: x * y), combination)
    except IndexError:
        return 0


# FIRST STAR
print(get_multiplication(SUM_VALUE, 2))

# SECOND STAR
print(get_multiplication(SUM_VALUE, 3))
