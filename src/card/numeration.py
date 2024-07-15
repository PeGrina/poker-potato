from src.utils.available import available_ranks, available_suits
from src.card.card import Card


def get_number_by_card(card):
    return available_suits.index(card.suit) * 13 + available_ranks.index(card.rank)


def get_card_by_number(number):
    return Card(available_ranks[number % len(available_ranks)], available_suits[number // len(available_ranks)])
