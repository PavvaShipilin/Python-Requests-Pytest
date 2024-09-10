import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd703d97eb864d66f622b39fac181fd91'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5372' 

def test_status_code ():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response.status_code == 200