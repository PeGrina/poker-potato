import unittest

from game.card.card import Card


def create_card(rank, suit):
    print(rank, suit)
    return Card(rank, suit)


class TestCard(unittest.TestCase):
    def test_invalid_rank_and_suit(self):
        print("Ok")
        self.assertRaises(Exception, create_card, "-", "F")

    def test_invalid_rank(self):
        self.assertRaises(Exception, create_card, "22", "F")

    def test_invalid_len_suit(self):
        self.assertRaises(Exception, create_card, "2", "G")

    def test_good(self):
        create_card("A", "H")


if __name__ == "__main__":
    unittest.main()
