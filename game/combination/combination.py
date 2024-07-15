# Combination is a pair of (Nominal of Combination, 5 Cards in order) Also 5 cards in order means that at the start
# of combo selected that cards who are play in nominal, then other cards in non-increasing order

from utils.utils import check_card
from game.combination.determine_combination import determine_combination
from game.card.card import Card
from game.combination.rank_names import get_combination_name_by_rank


class Combination:
    #   field of class
    #   cards - 5 cards
    #   rank_combination - Rank of combination for more details look RankCombinations.txt
    #   sorted_cards - order of cards

    def __init__(self):
        pass

    def is_correct_input(self):
        if len(self.cards) != 5:
            raise Exception("Not valid number of cards")
        for card in self.cards:
            if not check_card(card):
                raise Exception("Your input contains invalid data")

    def __init__(self, cards):
        self.cards = cards
        self.is_correct_input()
        _rank_combination, _sorted_cards = determine_combination(self.cards)
        self.rank_combination = _rank_combination
        self.sorted_cards = _sorted_cards

    def get_sorted_cards_str(self):
        cards = []
        for card in self.sorted_cards:
            cards.append(str(card))
        return cards

    def get_rank_str(self):
        return get_combination_name_by_rank[self.rank_combination]

    def print_sorted_combination(self):
        print('[', end='')
        print(", ".join([str(card) for card in self.sorted_cards]), end='')
        print(']')

    def __eq__(self, other):
        if self.rank_combination != other.rank_combination:
            return False

        for j in range(0, len(self.sorted_cards)):
            if self.sorted_cards[j].get_rank() != other.sorted_cards[j].get_rank():
                return False

        return True

    def __lt__(self, other):
        if self == other:
            return False
        if self.rank_combination == other.rank_combination:
            return self.sorted_cards < other.sorted_cards
        return self.rank_combination < other.rank_combination
