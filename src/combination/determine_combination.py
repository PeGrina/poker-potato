def rotate(l, n):
    return l[n:] + l[:n]


def determine_combination(cards):
    if len(cards) != 5:
        raise Exception("Incorrect number of cards")

    ordered_cards = sorted(cards, reverse=True)

    is_flush = all(card.suit == ordered_cards[0].suit for card in ordered_cards)
    was_tricky = False
    is_straight = True

    for i in range(len(ordered_cards) - 1):
        if ordered_cards[i + 1].rank != ordered_cards[i].rank - 1:
            if not (ordered_cards[i].rank == 14 and ordered_cards[i + 1].rank == 5):  # Ace and 5
                is_straight = False
            else:
                was_tricky = True

    if is_straight and is_flush:
        if was_tricky:
            ordered_cards = rotate(ordered_cards, 1)
        if ordered_cards[0].rank == 14:
            return 9, ordered_cards
        return 8, ordered_cards

    rank_count = {}
    for card in ordered_cards:
        if card.rank in rank_count:
            rank_count[card.rank] += 1
        else:
            rank_count[card.rank] = 1

    sorted_counts = sorted(((count, rank) for rank, count in rank_count.items()), reverse=True)

    # Creating the ordered list of cards for non-straight and non-flush hands
    order_without_flush_and_straight = []
    for count, rank in sorted_counts:
        order_without_flush_and_straight.extend(card for card in ordered_cards if card.rank == rank)

    if sorted_counts[0][0] == 4:
        return 7, order_without_flush_and_straight

    if sorted_counts[0][0] == 3 and len(sorted_counts) > 1 and sorted_counts[1][0] == 2:
        return 6, order_without_flush_and_straight

    if is_flush:
        return 5, ordered_cards

    if is_straight:
        if was_tricky:
            return 4, rotate(ordered_cards, 1)
        return 4, ordered_cards

    if sorted_counts[0][0] == 3:
        return 3, order_without_flush_and_straight

    if sorted_counts[0][0] == 2 and len(sorted_counts) > 1 and sorted_counts[1][0] == 2:
        return 2, order_without_flush_and_straight

    if sorted_counts[0][0] == 2:
        return 1, order_without_flush_and_straight

    return 0, ordered_cards
