from flask import Flask, jsonify, request
from k_dramas_data import dramas
from utils import search_dramas, get_drama_name

app = Flask(__name__)

# Get information
@app.route('/')
def hello():
    return {'hello': 'Marker!'}

@app.route('/dramas')
def get_dramas():
    return jsonify(dramas)

# Search for drama by name
@app.route('/dramas/<drama_name>', methods=['GET'])
def get_drama(drama_name):
    drama = search_dramas(drama_name, dramas)
    if drama:
        return jsonify(drama)
    else:
        return jsonify({"error": "Drama not found"}), 404


# Add new dramas
@app.route('/dramas', methods=['POST'])
def add_drama():
    drama = request.get_json()
    dramas.append(drama)
    return drama

# Update new dramas
@app.route('/dramas/<drama_name>', methods=['PUT'])
def update_drama(drama_name):
    drama_to_update = request.get_json()
    index = get_drama_name(drama_name, dramas)
    dramas[index] = drama_to_update
    return jsonify(dramas[index])

# Delete a drama
@app.route('/dramas/<drama_name>', methods=['DELETE'])
def delete_drama(drama_name):
    index = get_drama_name(drama_name, dramas)
    deleted = dramas.pop(index)
    return jsonify(deleted)







if __name__ == '__main__':
    app.run(debug=True)