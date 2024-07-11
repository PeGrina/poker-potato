def check_elements_same_type(array):
    if len(array) == 0:
        return True
    checked_list = filter(lambda x: type(x) == type(array[0]), array)
    return len(checked_list) == len(array)


def check_is_it_card(card):
    from card import Card
    _card = Card(2, 'D')
    return type(card) == type(_card)
