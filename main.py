from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello it's api for poker, that can calculate some useful things"}


@app.post("/select_winner/")
async def select_winner(players_count: int, table: list[str], players: list[list[str]]):
    print(table, players)
    if len(players) != players_count:
        raise HTTPException(status_code=404, detail="players count is wrong")
    return {"players": players_count}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

