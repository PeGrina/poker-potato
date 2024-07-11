# Combination is a pair of (Nominal of Combination, 5 Cards in order) Also 5 cards in order means that at the start
# of combo selected that cards who are play in nominal, then other cards in non-increasing order

from utils.utils import check_is_it_card
from determine_combination import determine_combination
from game.card.card import Card


class Combination:
    #   field of class
    #   cards - 5 cards
    #   rank_combination - Rank of combination for more details look RankCombinations.txt
    #   sorted_cards - order of cards

    def __init__(self):
        pass

    def is_correct_input(self):
        assert (len(self.cards) == 5)
        for card in self.cards:
            assert check_is_it_card(card)

    def __init__(self, cards):
        self.cards = cards
        self.is_correct_input()
        _rank_combination, _sorted_cards = determine_combination(self.cards)
        self.rank_combination = _rank_combination
        self.sorted_cards = _sorted_cards

    def __lt__(self, other):
        if self.rank_combination == other.rank_combination:
            return self.sorted_cards < other.sorted_cards
        return self.rank_combination < other.rank_combination
