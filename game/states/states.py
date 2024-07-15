from pydantic import BaseModel


class SPokerState(BaseModel):
    number_of_players: int
    players: list[list[str]]
    table: list[str]


class SSelectWinnerResponse(BaseModel):
    players_top_combination_rank: list[str]
    players_top_combination_cards: list[list[str]]
    winner: list[int]


class SProbabilityCountResponse(BaseModel):
    pass
