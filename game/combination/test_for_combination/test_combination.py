import unittest

from game.combination.combination import Combination
from game.card.card import Card
from game.combination.rank_by_name import get_combination_rank_by_name


def create_combination(cards: list[Card]):
    return Combination(cards)


class TestCombination(unittest.TestCase):
    def test_not_enough_len(self):
        self.assertRaises(Exception, create_combination,
                          [Card('2', 'H'), Card('J', 'D'), Card('5', 'S'), Card('K', 'C')])

    def test_too_more_len(self):
        self.assertRaises(Exception, create_combination,
                          [Card('2', 'H'), Card('J', 'D'), Card('5', 'S'), Card('K', 'C'), Card('2', 'H'),
                           Card('J', 'D'), Card('5', 'S'), Card('K', 'C')])

    def test_High_card(self):
        c = create_combination([Card('2', 'H'), Card('J', 'D'), Card('5', 'S'), Card('K', 'C'), Card('8', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["High_card"])

    def test_one_pair1(self):
        c = create_combination([Card('2', 'H'), Card('2', 'D'), Card('5', 'S'), Card('K', 'C'), Card('8', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["One_pair"])

    def test_one_pair2(self):
        c = create_combination([Card('2', 'H'), Card('3', 'D'), Card('5', 'S'), Card('A', 'C'), Card('A', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["One_pair"])

    def test_two_pairs1(self):
        c = create_combination([Card('2', 'H'), Card('2', 'D'), Card('5', 'S'), Card('K', 'C'), Card('K', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Two_pairs"])

    def test_two_pairs2(self):
        c = create_combination([Card('2', 'H'), Card('4', 'D'), Card('4', 'S'), Card('A', 'C'), Card('A', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Two_pairs"])

    def test_set1(self):
        c = create_combination([Card('2', 'H'), Card('A', 'D'), Card('5', 'S'), Card('5', 'C'), Card('5', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Three_of_a_kind"])

    def test_set2(self):
        c = create_combination([Card('7', 'H'), Card('7', 'D'), Card('5', 'S'), Card('7', 'C'), Card('8', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Three_of_a_kind"])

    def test_straight1(self):
        c = create_combination([Card('2', 'H'), Card('5', 'D'), Card('4', 'S'), Card('3', 'C'), Card('A', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Straight"])

    def test_straight2(self):
        c = create_combination([Card('A', 'H'), Card('J', 'D'), Card('T', 'S'), Card('K', 'C'), Card('Q', 'D')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Straight"])

    def test_straight3(self):
        c = create_combination([Card('7', 'H'), Card('8', 'H'), Card('T', 'H'), Card('9', 'H'), Card('6', 'C')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Straight"])

    def test_straight4(self):
        c = create_combination([Card('7', 'H'), Card('8', 'H'), Card('T', 'H'), Card('9', 'H'), Card('J', 'C')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Straight"])

    def test_flush1(self):
        c = create_combination([Card('7', 'H'), Card('8', 'H'), Card('T', 'H'), Card('9', 'H'), Card('5', 'H')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Flush"])

    def test_flush2(self):
        c = create_combination([Card('A', 'C'), Card('8', 'C'), Card('T', 'C'), Card('9', 'C'), Card('5', 'C')])

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Flush"])

    def test_full_house1(self):
        c = create_combination([Card('5', 'C'), Card('A', 'D'), Card('A', 'H'), Card('5', 'C'), Card('5', 'H')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Full_house"])

    def test_full_house2(self):
        c = create_combination([Card('A', 'C'), Card('A', 'D'), Card('A', 'H'), Card('5', 'C'), Card('5', 'H')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Full_house"])

    def test_full_house3(self):
        c = create_combination([Card('K', 'C'), Card('K', 'D'), Card('A', 'H'), Card('A', 'C'), Card('K', 'H')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Full_house"])

    def test_four_of_a_kind1(self):
        c = create_combination([Card('K', 'D'), Card('K', 'C'), Card('K', 'H'), Card('K', 'S'), Card('A', 'H')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Four_of_a_kind"])

    def test_four_of_a_kind1(self):
        c = create_combination([Card('A', 'D'), Card('A', 'C'), Card('A', 'H'), Card('A', 'S'), Card('K', 'H')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Four_of_a_kind"])

    def test_straight_flush1(self):
        c = create_combination([Card('A', 'H'), Card('2', 'H'), Card('4', 'H'), Card('5', 'H'), Card('3', 'H')])
        c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Straight_flush"])

    def test_straight_flush2(self):
        c = create_combination([Card('6', 'H'), Card('2', 'H'), Card('4', 'H'), Card('5', 'H'), Card('3', 'H')])
        c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Straight_flush"])

    def test_royal_flush1(self):
        c = create_combination([Card('A', 'H'), Card('T', 'H'), Card('Q', 'H'), Card('K', 'H'), Card('J', 'H')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Royal_flush"])

    def test_royal_flush2(self):
        c = create_combination([Card('A', 'S'), Card('T', 'S'), Card('Q', 'S'), Card('K', 'S'), Card('J', 'S')])
        # c.print_sorted_combination()

        self.assertEqual(len(c.sorted_cards), 5)
        self.assertEqual(c.rank_combination, get_combination_rank_by_name["Royal_flush"])


if __name__ == "__main__":
    unittest.main()
