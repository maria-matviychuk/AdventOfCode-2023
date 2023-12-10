from d9.day9_input import DATA

test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def read_numbers(data):
    return [int(s) for s in data.split(" ")]


def build_history(numbers):
    new_matrix = []
    i = 0
    new_matrix.append(numbers)
    while not all([x == 0 for x in new_matrix[i]]):
        new_matrix.append([new_matrix[i][idx + 1] - new_matrix[i][idx] for idx in range(len(new_matrix[i]) - 1)])
        i += 1
    return new_matrix


def get_next_prediction(all_lines):
    last_prediction = 0
    count = len(all_lines)
    for idx in range(count):
        last_prediction = all_lines[count - idx - 1][-1] + last_prediction
    return last_prediction


def get_prev_prediction(all_lines):
    last_prediction = 0
    count = len(all_lines)
    for idx in range(count):
        last_prediction = all_lines[count - idx - 1][0] - last_prediction
    return last_prediction


def first_res(data):
    res = 0
    lines = data.strip().splitlines()
    for line in lines:
        numbers = read_numbers(line)
        history = build_history(numbers)
        res += get_next_prediction(history)
    return res


def second_res(data):
    res = 0
    lines = data.strip().splitlines()
    for line in lines:
        numbers = read_numbers(line)
        history = build_history(numbers)
        res += get_prev_prediction(history)
    return res


assert first_res(test_input) == 114
assert first_res(DATA) == 1868368343

assert second_res(test_input) == 2
assert second_res(DATA) == 1022
