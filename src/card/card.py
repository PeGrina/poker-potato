from src.utils.available import available_ranks, available_suits

from src.card.get_card_names import get_name_by_rank, get_rank_by_name, get_suit_by_name, get_name_by_suit


class Card:
    def create_card(self, _rank: str, _suit: str):
        if type(_rank) != str or type(_suit) != str:
            raise TypeError("Argument must be of type str")
        if not _rank in available_ranks and not _suit in available_suits:
            raise Exception("Rank and Suit are invalid")
        if not _suit in available_suits:
            raise Exception("Suit is invalid")
        if not _rank in available_ranks:
            raise Exception("Rank is invalid")

        self.rank = get_rank_by_name[_rank]
        self.suit = get_suit_by_name[_suit]

    def __init__(self, _rank, _suit):
        self.suit = None
        self.rank = None
        self.create_card(_rank, _suit)

    def get_rank(self):  # get highest value for rank
        return self.rank

    def get_suit(self):  # just getter for suit
        return self.suit

    def get_rank_name(self):
        return get_name_by_rank[self.rank]

    def get_suit_name(self):
        return get_suit_by_name[self.suit]

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    def __str__(self):
        return "(" + self.get_rank_name() + str(", ") + self.get_suit_name() + ")"
