from game.combination.combination import Combination


class Selector:

    def __init__(self, cards):
        self.best_combination = None
        self.cards = cards
        self.select_combination()

    def select_combination(self):
        self.best_combination = None
        for i in range(0, len(self.cards)):
            for j in range(i + 1, len(self.cards)):
                for x in range(j + 1, len(self.cards)):
                    for y in range(x + 1, len(self.cards)):
                        for w in range(y + 1, len(self.cards)):
                            cards = [self.cards[i], self.cards[j], self.cards[x], self.cards[y], self.cards[w]]
                            combination = Combination(cards)
                            if self.best_combination is None or self.best_combination < combination:
                                self.best_combination = combination
