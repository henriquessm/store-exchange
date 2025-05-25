from fastapi import FastAPI
from currency_converter import CurrencyConverter
import time
import requests

app = FastAPI()


@app.get("/exchange/{f}/{to}")
async def exchange(f, to):
    c = CurrencyConverter()
    sell = c.convert(1, f, to)
    buy = c.convert(1, to, f)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    route = f'https://economia.awesomeapi.com.br/json/last/{f}-{to}'

    response = requests.get(route)
    response = response.json()
    sell = response[f + to]['ask']
    buy = response[f + to]['bid']

    return {"from": f, "to": to, "sell": sell, "buy": buy, "date": date}


@app.get("/")
async def root():
    return {"message": "Hello World"}