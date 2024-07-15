from src.utils.available import available_ranks, available_suits
from src.card.card import Card
from fastapi import HTTPException


def check_elements_same_type(array):
    if len(array) == 0:
        return True
    checked_list = filter(lambda x: type(x) == type(array[0]), array)
    return len(checked_list) == len(array)


def check_card(__card: Card) -> bool:
    _card = Card('2', 'D')
    if type(__card) != type(_card):
        return False

    if __card.rank not in available_ranks:
        return False

    if __card.suit not in available_suits:
        return False

    return True


def check_defined_card_str(__card: str) -> bool:
    rank = __card[0]
    suit = __card[1]
    if rank not in available_ranks:
        return False

    if suit not in available_suits:
        return False

    return True


def check_not_defined_card_str(__card: str) -> bool:
    rank = __card[0]
    suit = __card[1]
    if rank not in available_ranks and rank != '?':
        return False

    if suit not in available_suits and suit != '?':
        return False

    return True


def check_table(table):
    if type(table) != list:
        return False, "Incorrect data"

    if len(table) != 5:
        return False, "Incorrect data"

    for card in table:
        if type(card) != str:
            return False, "Incorrect data"

    return True, ""


def check_players(players, cnt):
    if type(players) != list:
        return False, "Incorrect data"

    if type(cnt) != int:
        return False, "Incorrect data"

    if len(players) != cnt:
        return False, "length of players and their count do not match"

    for i in range(len(players)):
        hand = players[i]
        if type(hand) != list:
            return False, "Incorrect data"

        if len(hand) != 2:
            return False, "Incorrect data"
        for card in hand:
            if type(card) != str:
                return False, "Incorrect data"
            if len(card) != 2:
                return False, "Incorrect data"

    return True, ""


def check_defined_cards_str(cards):
    for card in cards:
        if not check_defined_card_str(card):
            return False
    return True


def check_not_defined_cards_str(cards):
    for card in cards:
        if not check_not_defined_card_str(card):
            return False
    return True


def check_defined_cards(players, table):
    if not check_defined_cards_str(table):
        return HTTPException(400, "Invalid card in table")

    for hand in players:
        if not check_defined_cards_str(hand):
            return HTTPException(400, "Invalid card in hand")

    return 0


def check_not_defined_cards(players, table):
    if not check_not_defined_cards_str(table):
        return HTTPException(400, "Invalid card in table")

    for hand in players:
        if not check_not_defined_cards_str(hand):
            return HTTPException(400, "Invalid card in hand")

    return 0


def check_basic_cards_and_players(cnt, players, table):
    if cnt is None or players is None or table is None:
        return HTTPException(400, "Incorrect data")

    flag, _ = check_table(table)
    if not flag:
        return HTTPException(400, _)

    flag, _ = check_players(players, cnt)

    if not flag:
        return HTTPException(400, _)

    return 0
