from utils.available import available_ranks, available_suits

from get_card_rank import get_value_rank


class Card:

    def __init__(self):
        pass

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        assert self.suit in available_suits
        assert self.rank in available_ranks

    def get_rank(self):
        return get_value_rank[self.rank][-1]

    def get_ranks(self):
        return get_value_rank[self.rank]

    def __lt__(self, other):
        return self.get_rank() < other.get_rank()
