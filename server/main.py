from game.card.card import Card
from game.selector.selector import Selector
from game.combination.combination import Combination
from fastapi import FastAPI, HTTPException

from server.states import SPokerState, SSelectWinnerGet

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello it's api for poker, that can calculate some useful things"}


@app.get("/select_winner/")
async def select_winner(s: SPokerState):
    cnt = s.number_of_players
    players = s.players
    table = s.table
    if cnt is None or players is None or table is None:
        return HTTPException(400, "Incorrect data")

    if type(cnt) != int:
        return HTTPException(400, "Incorrect data")

    if type(players) != list:
        return HTTPException(400, "Incorrect data")

    if type(table) != list:
        return HTTPException(400, "Incorrect data")

    if len(players) != cnt:
        return HTTPException(400, "length of players and their count do not match")

    table_cards = []

    for card in table:
        if type(card) != str:
            return HTTPException(400, "Incorrect data")
        try:
            c = Card(card[0], card[1])
            table_cards.append(c)
        except Exception as error:
            return HTTPException(400, error)

    response = SSelectWinnerGet(players_top_combination_rank=[], players_top_combination_cards=[], winner=0)

    best_combo = None

    for i in range(len(players)):
        hand = players[i]
        if type(hand) != list:
            return HTTPException(400, "Incorrect data")

        player_cards = []

        if len(hand) != 2:
            return HTTPException(400, "Incorrect data")
        for card in hand:
            if len(card) != 2:
                return HTTPException(400, "Incorrect data")
            try:
                c = Card(card[0], card[1])
                player_cards.append(c)
            except Exception as error:
                return HTTPException(400, "error")

        summary = []
        for card in player_cards:
            summary.append(card)
        for card in table_cards:
            summary.append(card)

        s = Selector(summary)
        response.players_top_combination_rank.append(s.best_combination.get_rank_str())
        response.players_top_combination_cards.append(s.best_combination.get_sorted_cards_str())

        if best_combo is None or best_combo < s.best_combination:
            best_combo = s.best_combination
            response.winner = i
    return response
