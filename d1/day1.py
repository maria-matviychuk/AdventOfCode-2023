from d1.day1_input import DATA

test_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


test_input2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def first_res(data):
    res = 0
    for row in data.strip().splitlines():
        number1, number2 = 0, 0
        for el in row:
            if el.isdigit():
                number1 = int(el)
                break
        for el in row[::-1]:
            if el.isdigit():
                number2 = int(el)
                break

        full_number = number1 * 10 + number2
        res += full_number

    return res



MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_number(substring, el):
    if el.isdigit():
        return int(el)

    if len(substring) > 2:
        for key in MAPPING.keys():
            if key in substring:
                return MAPPING[key]


def second_res(data):
    res = 0
    for row in data.strip().splitlines():
        number1, number2 = 0, 0
        substring = ""
        for el in row:
            substring += el
            number1 = get_number(substring, el)
            if number1:
                break

        substring = ""
        for el in row[::-1]:
            substring = el + substring
            number2 = get_number(substring, el)
            if number2:
                break

        res += number1 * 10 + number2
    return res


assert first_res(test_input) == 142
assert first_res(DATA) == 54159

assert second_res(test_input2) == 281
assert second_res(DATA) == 53866