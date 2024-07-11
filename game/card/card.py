from utils.available import available_ranks, available_suits

from game.card.get_card_rank import get_value_rank


class Card:

    def __init__(self):
        pass

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if not rank in available_ranks and not suit in available_suits:
            raise Exception("Rank and Suit are invalid")

        if not self.suit in available_suits:
            raise Exception("Suit is invalid")
        if not self.rank in available_ranks:
            raise Exception("Rank is invalid")

    def get_rank(self):
        return get_value_rank[self.rank][-1]

    def get_suit(self):
        return self.suit

    def get_ranks(self):
        return get_value_rank[self.rank]

    def __lt__(self, other):
        if self.get_rank() == other.get_rank():
            return self.get_suit() < other.get_suit()
        return self.get_rank() < other.get_rank()

    def __str__(self):
        return "(" + str(self.rank) + str(", ") + str(self.suit) + ")"
