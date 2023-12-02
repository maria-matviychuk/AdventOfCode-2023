import re

from d2.day2_input import DATA

test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


IDEAL = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_count_game(games_row: str):
    games = games_row.split(";")
    for round in games:
        cubes = round.split(",")
        for cube in cubes:
            cube_amount = int(re.findall(r'\d+', cube)[0])
            for key in IDEAL.keys():
                if key in cube:
                    if IDEAL[key] < cube_amount:
                        return False
    return True


def first_res(data):
    res = 0
    for row in data.strip().splitlines():
        game_number, games_row = row.split(":")
        if is_count_game(games_row):
            game_id = int(game_number.replace("Game", "").strip())
            res += game_id

    return res


def get_minimum_cubes_power(games_row: str):
    minimum = {}
    games = games_row.split(";")
    for round in games:
        cubes = round.split(",")
        for cube in cubes:
            cube_amount = int(re.findall(r'\d+', cube)[0])
            for key in IDEAL.keys():
                if key in cube:
                    if key in minimum and minimum[key] > cube_amount:
                        continue
                    else:
                        minimum[key] = cube_amount

    power = 1
    for el in minimum.values():
        power *= el
    return power


def second_res(data):
    res = 0
    for row in data.strip().splitlines():
        game_number, games_row = row.split(":")
        res += get_minimum_cubes_power(games_row)

    return res


assert first_res(test_input) == 8
assert first_res(DATA) == 2720

assert second_res(test_input) == 2286
assert second_res(DATA) == 71535