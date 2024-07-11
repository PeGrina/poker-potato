class Card:

    def __init__(self):
        pass

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        return self.rank < other.rank
