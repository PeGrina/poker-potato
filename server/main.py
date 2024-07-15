from fastapi import FastAPI

from game.states.states import SPokerState
from utils.utils import check_defined_cards, check_not_defined_cards, check_basic_cards_and_players
from game.selector.select_winner import select_winner

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello it's api for poker, that can calculate some useful things"}


@app.get("/select_winner/")
async def select_winner(s: SPokerState):
    # cnt is required just for checking that all number of players if matches with the requested
    cnt, players, table = s.number_of_players, s.playes, s.table

    error = check_basic_cards_and_players(cnt, players, table)

    if error != 0:
        return error

    error = check_defined_cards(players, table)

    if error != 0:
        return error

    # players and table are valid
    # want to select winner with all defined cards

    response = select_winner(table, players)

    return response


@app.get("/count_probability/")
async def count_probability(s: SPokerState):
    cnt = s.number_of_players
    players = s.players
    table = s.table

    error = check_basic_cards_and_players(cnt, players, table)

    if error != 0:
        return error

    error = check_not_defined_cards(players, table)

    if error != 0:
        return error

    # players and table are valid

    # want to reorder cards to count in this order
    # 1) cards with defined suits and rank
    # 2) cards with defined rank
    # 3) cards with defined suit
    # 4) other cards




