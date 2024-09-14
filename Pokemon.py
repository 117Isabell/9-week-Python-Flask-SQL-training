import requests
from flask import Flask, render_template, request
import json  # Import the json module to handle JSON data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['POST'])
def get_pokemon():
    pokemon_number = request.form['pokemon']

    # API request
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(endpoint)

    # Accessing necessary data
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        height = float(data['height'])/10
        weight = float(data['weight'])/10
        image = data['sprites']['front_default']

        # Setup empty list to store information
        moves = []
        # Loop through and append info to list
        for move in data['moves']:
            moves.append(move['move']['name'])
        first_five_moves = ', '.join(moves[:5])

        formatted_data = (f"Name: {name}\n"
                          f"Height: {height} m\n"
                          f"Weight: {weight} kg\n"
                          f"Moves: {first_five_moves}\n"
                          f"Image: {image}\n"
                          )
        # Write the Pokémon data to a json file
        with open('pokemon_data.json', 'w') as f:
            json.dump(data, f, indent=4)

        # Write the key Pokémon data to a text file
        with open('pokemon_data.txt', 'w') as f:
            f.write(formatted_data)

        # Render the key data on the landing page
        return render_template('index.html', name=name, height=height, weight=weight, image=image, pokemon_number=pokemon_number)


if __name__ == '__main__':
    app.run(debug=True)