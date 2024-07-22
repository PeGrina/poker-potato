from src.card.card_numeration import *
from src.states.states import SProbabilityCountResponse
from src.selector.selector import Selector
from src.selector.select_winner import select_winner_with_cards
from fastapi import HTTPException

used = []
all_possible_cards = []
selected_cards = []
outcomes = 0
count_players = 0
response = SProbabilityCountResponse(players_probability_to_win=[], players_chance_combinations=[])


def change_response_by_selected_cards():
    global outcomes
    outcomes += 1
    global count_players, selected_cards, response
    players = []
    table = []

    for j in range(len(all_possible_cards) - 5, len(all_possible_cards)):
        table.append(get_card_by_number(selected_cards[j]))

    for i in range(count_players):
        hand = [get_card_by_number(selected_cards[i * 2]), get_card_by_number(selected_cards[i * 2 + 1])]
        players.append(hand)

    r = select_winner_with_cards(players, table)
    i = 0
    for combo_rank in r.players_top_combination_rank:
        response.players_chance_combinations[i][combo_rank] = response.players_chance_combinations[i].get(
            combo_rank, 0) + 1
        i += 1

    for _winner in r.winner:
        response.players_probability_to_win[_winner] += 1


def go_naive(i):
    if i == len(all_possible_cards):
        change_response_by_selected_cards()
        return

    for card in all_possible_cards[i]:
        if not used[card]:
            selected_cards[i] = card
            used[card] = True
            go_naive(i + 1)
            used[card] = False


def count_all_naive():
    global used, all_possible_cards, response
    used.clear()
    for i in range(52):
        used.append(0)

    go_naive(0)

    if outcomes == 0:
        return HTTPException(400, "You cards are not different")

    for i in range(len(response.players_probability_to_win)):
        response.players_probability_to_win[i] /= outcomes

    for i in range(len(response.players_chance_combinations)):
        for item in response.players_chance_combinations[i]:
            response.players_chance_combinations[i][item] /= outcomes

    return response


def count_probability(players, table):
    # want to reorder cards to define in this order
    # 1) cards with defined suits and rank
    # 2) cards with defined rank
    # 3) cards with defined suit
    # 4) other cards

    global all_possible_cards, selected_cards, response, count_players, outcomes

    response.players_probability_to_win = []
    response.players_chance_combinations = []

    count_players = len(players)
    all_possible_cards = []
    selected_cards = []
    outcomes = 0

    for j in range(count_players):
        response.players_probability_to_win.append(0)
        response.players_chance_combinations.append({})

    for hand in players:
        for card in hand:
            possible_cards = []
            if card[0] != '?' and card[1] != '?':
                possible_cards.append(get_number_by_card(Card(card[0], card[1])))
            elif card[0] == '?' and card[1] != '?':
                for rank in available_ranks:
                    possible_cards.append(get_number_by_card(Card(rank, card[1])))
            elif card[0] != '?' and card[1] == '?':
                for suit in available_suits:
                    possible_cards.append(get_number_by_card(Card(card[0], suit)))
            else:
                for i in range(52):
                    possible_cards.append(i)
            all_possible_cards.append(possible_cards)
            selected_cards.append(0)

    for card in table:
        possible_cards = []
        if card[0] != '?' and card[1] != '?':
            possible_cards.append(get_number_by_card(Card(card[0], card[1])))
        elif card[0] == '?' and card[1] != '?':
            for rank in available_ranks:
                possible_cards.append(get_number_by_card(Card(rank, card[1])))
        elif card[0] != '?' and card[1] == '?':
            for suit in available_suits:
                possible_cards.append(get_number_by_card(Card(card[0], suit)))
        else:
            for i in range(52):
                possible_cards.append(i)
        all_possible_cards.append(possible_cards)
        selected_cards.append(0)

    return count_all_naive()
