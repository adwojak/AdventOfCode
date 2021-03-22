from functools import reduce
from re import finditer

TREE_SYMBOL = "#"
BASE_MOVE_PATTERN = (3, 1)
MOVES_PATTERN_LIST = [(1, 1), BASE_MOVE_PATTERN, (5, 1), (7, 1), (1, 2)]
START_POSITION = (0, 0)


with open("input") as f:
    trees = []
    file_content = f.read().split("\n")
    ROWS_COUNT = len(file_content)
    LINE_LENGTH = len(file_content[0])
    [
        trees.append([tree.start() for tree in finditer("#", line)])
        for row, line in enumerate(file_content)
    ]


def get_toboggan_position(move_pattern, current_row):
    return (
        move_pattern[0] * current_row + START_POSITION[0],
        move_pattern[1] * current_row + START_POSITION[1],
    )


def get_encountered_trees(move_pattern):
    encountered_trees = 0
    for index, current_row in enumerate(range(int(ROWS_COUNT / move_pattern[1]))):
        toboggan_position = get_toboggan_position(move_pattern, current_row)
        if toboggan_position[0] % LINE_LENGTH in trees[toboggan_position[1]]:
            encountered_trees += 1
    return encountered_trees


def part_one():
    return get_encountered_trees(BASE_MOVE_PATTERN)


def part_two():
    return reduce(
        lambda a, b: a * b,
        [get_encountered_trees(move_pattern) for move_pattern in MOVES_PATTERN_LIST],
    )


print(part_one())
print(part_two())
