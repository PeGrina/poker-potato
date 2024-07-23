from fastapi import FastAPI

from src.selector.select_winner import select_winner
from src.states.states import SPokerState
from src.utils.utils import check_defined_cards, check_not_defined_cards, check_basic_cards_and_players
from src.probability.count_probability_using_random import count_probability

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello it's api for poker, that can calculate some useful things"}


@app.get("/select_winner/")
async def _select_winner(s: SPokerState):
    # cnt is required just for checking that all number of players if matches with the requested
    cnt, players, table = s.number_of_players, s.players, s.table

    error = check_basic_cards_and_players(cnt, players, table)

    if error != 0:
        return error

    error = check_defined_cards(players, table)

    if error != 0:
        return error

    # players and table are valid
    # want to select winner with all defined cards

    response = select_winner(players, table)

    # response is a json of
    # players top combination rank
    # players top combination cards
    # players who win

    return response


@app.get("/count_probability/")
async def _count_probability(s: SPokerState):
    cnt, players, table = s.number_of_players, s.players, s.table

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

    response = count_probability(players, table)

    return response




