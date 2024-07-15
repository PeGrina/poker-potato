from src.card.get_card_rank import get_value_rank


def is_one_pair(ordered_cards):
    for i in range(0, len(ordered_cards) - 1):
        if ordered_cards[i].get_rank() == ordered_cards[i + 1].get_rank():
            new_order = [ordered_cards[i], ordered_cards[i + 1]]
            for j in range(0, i):
                new_order.append(ordered_cards[j])
            for j in range(i + 2, len(ordered_cards)):
                new_order.append(ordered_cards[j])
            return True, new_order
    return False, ordered_cards


def is_two_pairs(ordered_cards):
    l = []
    d = {}
    for x in ordered_cards:
        l.append(x.get_rank())
        d[x.get_rank()] = d.get(x.get_rank(), 0)
        d[x.get_rank()] += 1

    l = sorted(l)
    l = l[::-1]

    pairs = []

    for i in range(len(l)):
        if d[l[i]] == 2:
            d[l[i]] -= 1
            pairs.append(l[i])

    if len(pairs) == 2:
        new_order = []

        for j in range(0, len(ordered_cards)):
            if ordered_cards[j].get_rank() in pairs:
                new_order.append(ordered_cards[j])

        for j in range(0, len(ordered_cards)):
            if ordered_cards[j].get_rank() not in pairs:
                new_order.append(ordered_cards[j])

        return True, new_order

    return False, ordered_cards


def is_three_of_a_kind(ordered_cards):
    for i in range(0, len(ordered_cards) - 2):
        if ordered_cards[i].get_rank() == ordered_cards[i + 1].get_rank() and ordered_cards[i + 1].get_rank() == ordered_cards[i + 2].get_rank():
            new_order = [ordered_cards[i], ordered_cards[i + 1], ordered_cards[i + 2]]
            for j in range(0, i):
                new_order.append(ordered_cards[j])
            for j in range(i + 3, len(ordered_cards)):
                new_order.append(ordered_cards[j])
            return True, new_order
    return False, ordered_cards


def is_straight(ordered_cards):
    for x in ordered_cards[0].get_ranks():
        for y in ordered_cards[1].get_ranks():
            for z in ordered_cards[2].get_ranks():
                for w in ordered_cards[3].get_ranks():
                    for d in ordered_cards[4].get_ranks():
                        t = [x, y, z, w, d]
                        t = sorted(t)
                        ok = True
                        for j in range(4):
                            if t[j + 1] - t[j] != 1:
                                ok = False
                                break

                        if ok:
                            t = t[::-1]
                            rem = {}
                            rem[d] = 4
                            rem[w] = 3
                            rem[z] = 2
                            rem[y] = 1
                            rem[x] = 0

                            new_order = []

                            for value in t:
                                new_order.append(ordered_cards[rem[value]])

                            return True, new_order

    return False, ordered_cards


def is_flush(ordered_cards):
    flag = True
    for card in ordered_cards:
        if card.get_suit() != ordered_cards[0].get_suit():
            flag = False
    return flag, ordered_cards


def is_full_house(ordered_cards):
    d = {}
    new_order = ordered_cards
    for j in range(0, len(ordered_cards)):
        d[ordered_cards[j].get_rank()] = d.get(ordered_cards[j].get_rank(), 0) + 1

    if d[ordered_cards[0].get_rank()] + d[ordered_cards[-1].get_rank()] != len(ordered_cards) or min(d[ordered_cards[0].get_rank()], d[
        ordered_cards[-1].get_rank()]) != 2 or max(d[ordered_cards[0].get_rank()], d[ordered_cards[-1].get_rank()]) != 3:
        return False, new_order

    if d[ordered_cards[0].get_rank()] == 3:
        return True, new_order

    new_order = new_order[::-1]
    return True, new_order


def is_four_of_a_kind(ordered_cards):
    for i in range(0, len(ordered_cards) - 3):
        if ordered_cards[i].get_rank() == ordered_cards[i + 1].get_rank() and ordered_cards[i + 1].get_rank() == ordered_cards[
            i + 2].get_rank() and ordered_cards[i + 2].get_rank() == ordered_cards[i + 3].get_rank():
            new_order = [ordered_cards[i], ordered_cards[i + 1], ordered_cards[i + 2], ordered_cards[i + 3]]
            for j in range(0, i):
                new_order.append(ordered_cards[j])
            for j in range(i + 4, len(ordered_cards)):
                new_order.append(ordered_cards[j])
            return True, new_order
    return False, ordered_cards


def is_straight_flush(ordered_cards):
    _f, _ = is_straight(ordered_cards)
    __f, __ = is_flush(ordered_cards)
    if _f and __f:
        return True, _
    return False, ordered_cards


def is_royal_flush(ordered_cards):
    _f, _ = is_straight_flush(ordered_cards)
    if _f:
        pass
    if _f and _[0].get_rank() == get_value_rank['A'][-1]:
        return True, _
    return False, ordered_cards


def determine_combination(cards):
    # order in non-increasing
    ordered_cards = sorted(cards)
    ordered_cards = ordered_cards[::-1]
    f, order = is_royal_flush(ordered_cards)
    if f:
        return 9, order
    f, order = is_straight_flush(ordered_cards)
    if f:
        return 8, order
    f, order = is_four_of_a_kind(ordered_cards)
    if f:
        return 7, order
    f, order = is_full_house(ordered_cards)
    if f:
        return 6, order
    f, order = is_flush(ordered_cards)
    if f:
        return 5, order
    f, order = is_straight(ordered_cards)
    if f:
        return 4, order
    f, order = is_three_of_a_kind(ordered_cards)
    if f:
        return 3, order
    f, order = is_two_pairs(ordered_cards)
    if f:
        return 2, order
    f, order = is_one_pair(ordered_cards)
    if f:
        return 1, order

    return 0, ordered_cards
