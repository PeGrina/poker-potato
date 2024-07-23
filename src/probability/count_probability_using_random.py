from src.card.card_numeration import *
from src.states.states import SProbabilityCountResponse
from src.selector.selector import Selector
from src.selector.select_winner import select_winner_with_cards
from fastapi import HTTPException
import random
import numpy as np


def change_response_by_selected_cards(selected_cards, count_players, response):
    table = [get_card_by_number(selected_cards[j]) for j in range(len(selected_cards) - 5, len(selected_cards))]
    players = [
        [get_card_by_number(selected_cards[i * 2]), get_card_by_number(selected_cards[i * 2 + 1])]
        for i in range(count_players)
    ]

    r = select_winner_with_cards(players, table)
    for i, combo_rank in enumerate(r.players_top_combination_rank):
        response.players_chance_combinations[i][combo_rank] = response.players_chance_combinations[i].get(combo_rank,
                                                                                                          0) + 1

    for _winner in r.winner:
        response.players_probability_to_win[_winner] += 1


def go_random(i, all_possible_cards, used, selected_cards, change_response_fn):
    if i == len(all_possible_cards):
        change_response_fn(selected_cards)
        return

    available_indices = [card for card in all_possible_cards[i] if not used[card]]
    if not available_indices:
        return

    card = random.choice(available_indices)
    selected_cards[i] = card
    used[card] = True
    go_random(i + 1, all_possible_cards, used, selected_cards, change_response_fn)
    used[card] = False


def count_all_iterative(all_possible_cards, selected_cards, count_players, response, iters=1500):
    used = np.zeros(52, dtype=bool)
    outcomes = 0

    def change_response_fn(selected_cards):
        nonlocal outcomes
        outcomes += 1
        change_response_by_selected_cards(selected_cards, count_players, response)

    for _ in range(iters):
        go_random(0, all_possible_cards, used, selected_cards, change_response_fn)

    if outcomes == 0:
        raise HTTPException(400, "Your cards are not different")

    response.players_probability_to_win = [x / outcomes for x in response.players_probability_to_win]
    for i in range(len(response.players_chance_combinations)):
        for key in response.players_chance_combinations[i]:
            response.players_chance_combinations[i][key] /= outcomes

    return response


def count_probability(players, table):
    count_players = len(players)
    all_possible_cards = []
    selected_cards = []

    response = SProbabilityCountResponse(
        players_probability_to_win=[0] * count_players,
        players_chance_combinations=[{} for _ in range(count_players)]
    )

    def add_possible_cards(card):
        if card[0] != '?' and card[1] != '?':
            return [get_number_by_card(Card(card[0], card[1]))]
        if card[0] == '?' and card[1] != '?':
            return [get_number_by_card(Card(rank, card[1])) for rank in available_ranks]
        if card[0] != '?' and card[1] == '?':
            return [get_number_by_card(Card(card[0], suit)) for suit in available_suits]
        return list(range(52))

    for hand in players:
        for card in hand:
            all_possible_cards.append(add_possible_cards(card))
            selected_cards.append(0)

    for card in table:
        all_possible_cards.append(add_possible_cards(card))
        selected_cards.append(0)

    return count_all_iterative(all_possible_cards, selected_cards, count_players, response)
