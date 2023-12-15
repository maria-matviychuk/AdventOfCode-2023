from collections import defaultdict

from d15.input import DATA

test_input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def get_hash(part):
    hash = 0
    for char in part:
        hash += ord(char)
        hash = hash * 17 % 256
    return hash


def first_res(data):
    res = 0
    parts = data.strip().split(",")
    for part in parts:
        res += get_hash(part)
    return res


def process_box(part, boxes):
    if "=" in part:
        label, focal_length = part.split("=")
        focal_length = int(focal_length)
        box_number = get_hash(label)
        boxes[box_number][label] = focal_length
    else:
        label = part.replace("-", "")
        box_number = get_hash(label)
        if label in boxes[box_number]:
            del boxes[box_number][label]


def second_res(data):
    res = 0
    parts = data.strip().split(",")
    boxes = defaultdict(dict)
    for part in parts:
        process_box(part, boxes)

    for box, value in boxes.items():
        for idx, label in enumerate(value):
            power = (box + 1) * (idx + 1) * value[label]
            res += power
    return res


assert first_res(test_input) == 1320
assert first_res(DATA) == 520500

assert second_res(test_input) == 145
assert second_res(DATA) == 213097
