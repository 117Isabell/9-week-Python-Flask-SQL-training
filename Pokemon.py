import requests
from pprint import pprint as pp

pokemon = input('pick a number')
# API request
endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
response = requests.get(endpoint)
data = response.json()

# Accessing necessary data
name = data['name']
height = float(data['height'])/10
weight = float(data['weight'])/10
image = data['sprites']['front_default']
print(image)

# Outputting information
print (f'Your Pokemon is called {name}, they are {height}m tall and weigh {weight}kgs')