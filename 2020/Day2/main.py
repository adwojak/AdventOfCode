from attrdict import AttrDict


def structurize_input_data(min_value, max_value, letter, password):
    return AttrDict(
        {
            "min_value": int(min_value),
            "max_value": int(max_value),
            "letter": letter,
            "password": password,
        }
    )


def parse_single_line(line):
    policy, password = line.split(":")
    occurences, letter = policy.split(" ")
    min_value, max_value = occurences.split("-")
    return structurize_input_data(min_value, max_value, letter, password)


with open("input") as f:
    input_data = [parse_single_line(line) for line in f.read().split("\n")]


def part_one():
    return len(
        [
            line
            for line in input_data
            if line.min_value <= line.password.count(line.letter) <= line.max_value
        ]
    )


def part_two():
    return len(
        [
            line
            for line in input_data
            if bool(line.password[line.min_value] == line.letter)
            ^ bool(line.password[line.max_value] == line.letter)
        ]
    )


print(part_one())
print(part_two())
