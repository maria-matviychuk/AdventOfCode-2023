import re

from d4.day4_input import DATA

test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def get_numbers(data):
    return re.findall(r'\d+', data)


def first_res(data):
    res = 0
    for row in data.strip().splitlines():
        points = 0
        real_row = row.split(":")[1]
        win_numbers_row, you_numbers_row = real_row.split("|")
        intersection = list(set(get_numbers(win_numbers_row)) & set(get_numbers(you_numbers_row)))
        for idx, _ in enumerate(intersection):
            if idx == 0:
                points = 1
            else:
                points *= 2
        res += points
    return res


def second_res(data):
    card_index = 0
    cards = []
    for row in data.strip().splitlines():
        card_index += 1
        real_row = row.split(":")[1]
        win_numbers_row, you_numbers_row = real_row.split("|")
        intersection = list(set(get_numbers(win_numbers_row)) & set(get_numbers(you_numbers_row)))

        cards.append(card_index)

        for el in cards:
            if el == card_index:
                for idx, _ in enumerate(intersection):
                    cards.append(idx + 1 + card_index)

    res = len(cards)
    return res


assert first_res(test_input) == 13
assert first_res(DATA) == 21959

assert second_res(test_input) == 30
assert second_res(DATA) == 5132675
