from d7.day7_input import DATA

test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


PRIORITIES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def get_sorted_hands(hands, weight_function):
    hands_weight = {}
    for hand in hands:
        hands_weight[hand] = weight_function(hand)

    tmp = dict(sorted(hands_weight.items(), key=lambda item: item[1], reverse=True))
    return list(tmp.keys())


def get_hand_precise_weight(hand, priorities=1):
    if priorities == 1:
        priorities = PRIORITIES
    else:
        priorities = PRIORITIES2
    weight = 0
    for i, char in enumerate(hand):
        b = pow(13, (len(hand) - i))
        weight += (len(priorities) - priorities.index(char)) * b
    return weight


def get_hand_weight(hand):
    if is_five_of_kind(hand):
        return pow(10, 10) * 7 + get_hand_precise_weight(hand)
    if is_four_of_kind(hand):
        return pow(10, 10) * 6 + get_hand_precise_weight(hand)
    if is_full_house(hand):
        return pow(10, 10) * 5 + get_hand_precise_weight(hand)
    if is_three_of_kind(hand):
        return pow(10, 10) * 4 + get_hand_precise_weight(hand)
    if is_two_pair(hand):
        return pow(10, 10) * 3 + get_hand_precise_weight(hand)
    if is_one_pair(hand):
        return pow(10, 10) * 2 + get_hand_precise_weight(hand)
    return get_hand_precise_weight(hand)


def is_five_of_kind(hand):
    return hand == len(hand) * hand[0]


def is_four_of_kind(hand):
    char_set = list(set(hand))
    return len(char_set) == 2 and (hand.count(char_set[0]) == 4 or hand.count(char_set[1]) == 4)


def is_full_house(hand):
    char_set = list(set(hand))
    return len(char_set) == 2 and (hand.count(char_set[0]) == 3 or hand.count(char_set[1]) == 3)


def is_three_of_kind(hand):
    char_set = list(set(hand))
    return len(char_set) == 3 and (hand.count(char_set[0]) == 3 or hand.count(char_set[1]) == 3 or hand.count(char_set[2]) == 3)


def is_two_pair(hand):
    char_set = list(set(hand))
    return len(char_set) == 3 and (hand.count(char_set[0]) != 3 or hand.count(char_set[1]) != 3 or hand.count(char_set[2]) != 3)


def is_one_pair(hand):
    char_set = set(hand)
    return len(char_set) == 4


def first_res(data):
    res = 0
    lines = data.strip().splitlines()
    hands_dict = {}
    for l in lines:
        hand, bid = l.strip().split(" ")
        hands_dict[hand] = int(bid)

    sorted_hands = get_sorted_hands(hands_dict.keys(), get_hand_weight)
    rank = len(hands_dict)
    for hand in sorted_hands:
        res += hands_dict[hand] * rank
        rank -= 1

    return res


PRIORITIES2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def is_five_of_kind2(hand):
    char_set = set(hand)
    return len(char_set) == 1 or (len(char_set) == 2 and "J" in char_set)


def is_combination(hand, function):
    char_set = list(set(hand))
    if "J" not in char_set:
        return function(hand)
    for char in char_set:
        if char != "J":
            if function(hand.replace("J", char)):
                return True
    return False


def is_one_pair2(hand):
    char_set = set(hand)
    return len(char_set) == 4 or (len(char_set) == 5 and "J" in char_set)


def get_hand_weight2(hand):
    if is_five_of_kind2(hand):
        return pow(10, 10) * 7 + get_hand_precise_weight(hand, 2)
    if is_combination(hand, is_four_of_kind):
        return pow(10, 10) * 6 + get_hand_precise_weight(hand, 2)
    if is_combination(hand, is_full_house):
        return pow(10, 10) * 5 + get_hand_precise_weight(hand, 2)
    if is_combination(hand, is_three_of_kind):
        return pow(10, 10) * 4 + get_hand_precise_weight(hand, 2)
    if is_combination(hand, is_two_pair):
        return pow(10, 10) * 3 + get_hand_precise_weight(hand, 2)
    if is_one_pair2(hand):
        return pow(10, 10) * 2 + get_hand_precise_weight(hand, 2)
    return get_hand_precise_weight(hand, 2)


def second_res(data):
    res = 0
    lines = data.strip().splitlines()
    hands_dict = {}
    for l in lines:
        hand, bid = l.strip().split(" ")
        hands_dict[hand] = int(bid)

    sorted_hands = get_sorted_hands(hands_dict.keys(), get_hand_weight2)
    rank = len(hands_dict)
    for hand in sorted_hands:
        res += hands_dict[hand] * rank
        rank -= 1

    return res


assert first_res(test_input) == 6440
assert first_res(DATA) == 247815719

assert second_res(test_input) == 5905
assert second_res(DATA) == 248747492
