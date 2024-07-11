# Combination is a pair of (Nominal of Combination, 5 Cards in order) Also 5 cards in order means that at the start
# of combo selected that cards who are play in nominal, then other cards in non-increasing order

from card import Card
from utils import check_elements_same_type, check_is_it_card


class Combination:
    #   field of class
    #   cards - 5 cards
    #   rank_combo - Ran

    def __init__(self):
        pass

    def is_correct_input(self):
        assert (len(self.cards) == 5)
        for card in self.cards:
            assert check_is_it_card(card)

    def __init__(self, cards):
        self.cards = cards
        self.is_correct_input()

    def __lt__(self, other):
