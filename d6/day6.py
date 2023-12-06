import math
import re

from d6.day6_input import DATA

test_input = """
Time:      7  15   30
Distance:  9  40  200
"""


def get_numbers(data):
    return [int(s) for s in re.findall(r'\d+', data)]


def first_res(data):
    res = 1
    lines = data.strip().splitlines()
    times = get_numbers(lines[0])
    distances = get_numbers(lines[1])
    input = zip(times, distances)
    for el in input:
        amount = get_ways_to_win(el[0], el[1])
        res *= amount

    return res


def get_ways_to_win(time, distance):
    min_time = math.ceil(distance / time)
    min_time_to_hold = 0
    max_time_to_hold = time - min_time
    for i in range(min_time, time - min_time):
        max_distance = i * (time - i)
        if max_distance > distance:
            min_time_to_hold = i
            break

    for i in range(time - min_time, min_time, -1):
        max_distance = i * (time - i)
        if max_distance > distance:
            max_time_to_hold = i
            break

    return max_time_to_hold - min_time_to_hold + 1


def second_res(data):
    lines = data.strip().splitlines()
    time = int(lines[0].replace("Time:", "").strip().replace(" ", ""))
    distance = int(lines[1].replace("Distance:", "").strip().replace(" ", ""))
    res = get_ways_to_win(time, distance)
    return res


assert first_res(test_input) == 288
assert first_res(DATA) == 741000

assert second_res(test_input) == 71503
assert second_res(DATA) == 38220708
