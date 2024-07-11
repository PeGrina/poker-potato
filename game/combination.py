# Combination is a pair of (Nominal of Combination, 5 Cards in order) Also 5 cards in order means that at the start
# of combo selected that cards who are play in nominal, then other cards in non-increasing order

from utils.utils import check_is_it_card

class Combination:
    #   field of class
    #   cards - 5 cards
    #   rank_combo - Rank of combination for more details look RankCombinations.txt
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

    def __lt__(self, other):
        # TODO: add less operator
        pass
