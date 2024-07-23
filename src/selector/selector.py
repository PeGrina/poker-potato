from src.combination.combination import Combination
from itertools import combinations

class Selector:

    def __init__(self, cards):
        self.best_combination = None
        self.cards = cards
        self.select_combination()

    def select_combination(self):
        self.best_combination = None
        for combo in combinations(self.cards, 5):
            combination = Combination(combo)
            if self.best_combination is None or self.best_combination < combination:
                self.best_combination = combination
