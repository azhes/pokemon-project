import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')
print(response)
data = response.json()
print(data['stats'][0]['stat']['name'])