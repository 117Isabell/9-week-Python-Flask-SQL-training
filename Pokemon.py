import requests
from flask import Flask, render_template, request
from pprint import pprint as pp

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['POST'])
def get_pokemon():
    pokemon = requests.form['pokemon']

# API request
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
    response = requests.get(endpoint)


    if response.status_code == 200:
        data = response.json()
# Accessing necessary data
        name = data['name']
        height = float(data['height'])/10
        weight = float(data['weight'])/10
        image = data['sprites']['front_default']
        print(image)
        return render_template('index.html', name=name, height=height, weight=weight, image=image)
    else:
        error = "Pokémon not found!"
        return render_template('index.html', error=error)

# Outputting information
        print (f'Your Pokemon is called {name}, they are {height}m tall and weigh {weight}kgs')

if __name__ == '__main__':
    app.run(debug=True)