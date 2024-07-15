from src.states.states import SSelectWinnerResponse
from src.card.card import Card
from src.selector.selector import Selector


def select_winner(players, table):
    # print(table, players)
    table_cards = []
    players_cards = []

    for card in table:
        c = Card(card[0], card[1])
        table_cards.append(c)

    for i in range(len(players)):
        player_cards = []

        for card in players[i]:
            c = Card(card[0], card[1])
            player_cards.append(c)

        players_cards.append(player_cards)

    response = select_winner_with_cards(players_cards, table_cards)

    return response


def select_winner_with_cards(players_cards, table_cards):
    response = SSelectWinnerResponse(players_top_combination_rank=[], players_top_combination_cards=[], winner=[])

    best_combo = None

    for i in range(len(players_cards)):
        summary = []
        for card in players_cards[i]:
            summary.append(card)
        for card in table_cards:
            summary.append(card)

        s = Selector(summary)
        response.players_top_combination_rank.append(s.best_combination.get_rank_str())
        response.players_top_combination_cards.append(s.best_combination.get_sorted_cards_str())

        if best_combo is None or best_combo < s.best_combination:
            best_combo = s.best_combination
            response.winner = [i]
        elif best_combo == s.best_combination:
            response.winner.append(i)
    return response
