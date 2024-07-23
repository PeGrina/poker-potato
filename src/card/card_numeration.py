from src.utils.available import available_ranks, available_suits
from src.card.card import Card
from src.card.get_card_names import get_name_by_rank, get_name_by_suit


def get_number_by_card(card):
    return available_suits.index(get_name_by_suit[card.suit]) * 13 + available_ranks.index(get_name_by_rank[card.rank])


def get_card_by_number(number):
    return Card(available_ranks[number % len(available_ranks)], available_suits[number // len(available_ranks)])
