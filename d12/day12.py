from functools import cache

from d12.day12_input import DATA

test_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


@cache
def get_string_arrangement(data: str, groups: tuple, started_group=False) -> int:
    groups = list(groups)
    if sum(groups) > len(data):
        return 0

    if len(groups) == 0:
        if "#" not in data:
            return 1
        return 0

    if len(data) == 1 and data != "?":
        if data == "#" and len(groups) == 1 and groups[0] == 1:
            return 1
        elif data == "." and (len(groups) == 0 or (len(groups) == 1 and groups[0] == 0)):
            return 1
        return 0

    if data[0] == "#":
        if groups[0] == 0:
            return 0
        started_group = True
        return get_string_arrangement(data[1:], tuple([groups[0] - 1] + groups[1:]), started_group)
    elif data[0] == ".":
        if groups[0] == 0:
            started_group = False
            return get_string_arrangement(data[1:], tuple(groups[1:]), started_group)
        if started_group:
            return 0
        return get_string_arrangement(data[1:], tuple(groups), started_group)
    else:
        return get_string_arrangement("#" + data[1:], tuple(groups), started_group) + get_string_arrangement("." + data[1:], tuple(groups), started_group)


def first_res(data: str) -> int:
    res = 0
    for line in data.strip().splitlines():
        schema, group_line = line.split(" ")
        groups = [int(el) for el in group_line.split(",")]
        res += get_string_arrangement(schema, tuple(groups))
    return res


def second_res(data: str) -> int:
    res = 0
    for line in data.strip().splitlines():
        schema, group_line = line.split(" ")
        long_group_line = ((group_line + ",") * 5)[:-1]
        groups = [int(el) for el in long_group_line.split(",")]
        long_schema = ((schema + "?") * 5)[:-1]
        res += get_string_arrangement(long_schema, tuple(groups))
    return res


assert first_res(test_input) == 21
assert first_res(DATA) == 7173

assert second_res(test_input) == 525152
assert second_res(DATA) == 29826669191291
