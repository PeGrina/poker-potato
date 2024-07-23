from src.states.states import SSelectWinnerResponse
from src.card.card import Card
from src.selector.selector import Selector


def select_winner(players, table):
    table_cards = [Card(card[0], card[1]) for card in table]
    players_cards = [[Card(card[0], card[1]) for card in player] for player in players]
    return select_winner_with_cards(players_cards, table_cards)


def select_winner_with_cards(players_cards, table_cards):
    response = SSelectWinnerResponse(players_top_combination_rank=[], players_top_combination_cards=[], winner=[])
    best_combo = None

    for i, player in enumerate(players_cards):
        summary = player + table_cards
        s = Selector(summary)
        response.players_top_combination_rank.append(s.best_combination.get_rank_str())
        response.players_top_combination_cards.append(s.best_combination.get_sorted_cards_str())

        if best_combo is None or best_combo < s.best_combination:
            best_combo = s.best_combination
            response.winner = [i]
        elif best_combo == s.best_combination:
            response.winner.append(i)

    return response
