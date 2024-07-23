def rotate(l, n):
    return l[n:] + l[:n]


def determine_combination(cards):
    if len(cards) != 5:
        raise Exception("Incorrect number of cards")

    ordered_cards = sorted(cards, reverse=True)

    is_flush = True
    is_straight = True
    was_tricky = False

    cnt_rank = []

    for i in range(len(ordered_cards) - 1):
        if ordered_cards[i + 1].suit != ordered_cards[0].suit:
            is_flush = False

        if ordered_cards[i + 1].rank != ordered_cards[i].rank - 1:
            if not (ordered_cards[i].rank == 14 and ordered_cards[i + 1].rank == 5):  # Ace and 5
                is_straight = False
            else:
                was_tricky = True

    if is_straight and is_flush:
        best_order = ordered_cards
        if was_tricky:
            best_order = rotate(ordered_cards, 1)

        if best_order[0].rank == 14:
            return 9, best_order

        return 8, best_order

    order_without_flush_and_straight = []

    for i in range(len(ordered_cards)):
        if len(cnt_rank) == 0:
            cnt_rank.append([1, ordered_cards[i].rank])
        else:
            if ordered_cards[i].rank == cnt_rank[-1][1]:
                cnt_rank[-1][0] += 1
            else:
                cnt_rank.append([1, ordered_cards[i].rank])

    ordered_cnt = sorted(cnt_rank, reverse=True)

    # sorry, я платница

    for i in range(len(ordered_cnt)):
        for j in range(len(ordered_cards)):
            if ordered_cnt[i][1] == ordered_cards[j].rank:
                order_without_flush_and_straight.append(ordered_cards[j])

    if len(ordered_cnt) > 0 and ordered_cnt[0][0] == 4:
        return 7, order_without_flush_and_straight

    if len(ordered_cnt) > 1 and ordered_cnt[0][0] == 3 and ordered_cnt[1][0] == 2:
        return 6, order_without_flush_and_straight

    if is_flush:
        return 5, ordered_cards

    if is_straight:
        return 4, ordered_cards

    if len(ordered_cnt) > 0 and ordered_cnt[0][0] == 3:
        return 3, order_without_flush_and_straight

    if len(ordered_cnt) > 0 and ordered_cnt[0][0] == 2 and ordered_cnt[1][0] == 2:
        return 2, order_without_flush_and_straight

    if len(ordered_cnt) > 0 and ordered_cnt[0][0] == 2:
        return 1, order_without_flush_and_straight

    return 0, ordered_cards
