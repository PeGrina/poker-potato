from src.utils.available import available_ranks, available_suits

from src.card.get_card_rank import get_value_rank


class Card:

    def create_card(self, _rank: str, _suit: str):
        self.rank = _rank
        self.suit = _suit

        if not self.rank in available_ranks and not _suit in available_suits:
            raise Exception("Rank and Suit are invalid")
        if not self.suit in available_suits:
            raise Exception("Suit is invalid")
        if not self.rank in available_ranks:
            raise Exception("Rank is invalid")

    def __init__(self, rank, suit):
        self.suit = None
        self.rank = None
        self.create_card(rank, suit)

    def get_rank(self):  # get highest value for rank
        return get_value_rank[self.rank][-1]

    def get_suit(self):  # just getter for suit
        return self.suit

    def get_ranks(self):  # get all values for rank
        return get_value_rank[self.rank]

    def __lt__(self, other):
        if self.get_rank() == other.get_rank():
            return self.get_suit() < other.get_suit()
        return self.get_rank() < other.get_rank()

    def __str__(self):
        return "(" + str(self.rank) + str(", ") + str(self.suit) + ")"
