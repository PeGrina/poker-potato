def check_elements_same_type(array):
    if len(array) == 0:
        return True
    checked_list = filter(lambda x: type(x) == type(array[0]), array)
    return len(checked_list) == len(array)


def check_is_it_card(__card):
    from game.card.card import Card
    from utils.available import available_ranks, available_suits
    _card = Card('2', 'D')
    if type(__card) != type(_card):
        return False

    if __card.rank not in available_ranks:
        return False

    if __card.suit not in available_suits:
        return False

    return True
