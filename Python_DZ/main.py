import requests

URL =  'https://api.pokemonbattle.ru/v2'
TOKEN = 'd703d97eb864d66f622b39fac181fd91'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
body_generate = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_generate)
print(response.text)

pokemon_id = response.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": pokemon_id,
}


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)