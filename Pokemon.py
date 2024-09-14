import requests
from flask import Flask, render_template, request
import os
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['POST'])
def get_pokemon():
    pokemon = request.form['pokemon']

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
        return render_template('index.html', name=name, height=height, weight=weight, image=image)


if __name__ == '__main__':
    app.run(debug=True)