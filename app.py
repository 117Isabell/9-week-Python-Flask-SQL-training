# Please kindly check out the readme file for better experience

from flask import Flask, jsonify, request
from k_dramas_data import dramas
from db_utils import search_dramas, get_drama_name

app = Flask(__name__)

# Get information
@app.route('/')
def hello():
    return {'Greeting': 'Hello, you are finally here!'}

# Get all the dramas from db
@app.route('/dramas')
def get_dramas():
    return jsonify(dramas)

# Search for dramas by names
@app.route('/dramas/<name>', methods=['GET'])
def get_drama(name):
    drama = search_dramas(name, dramas)
    if drama:
        return jsonify(drama)
    else:
        return jsonify({"error": "😞 Drama not found! 🚫"}), 404

# Add a new drama by its name
@app.route('/dramas', methods=['POST'])
def add_drama():
    drama = request.get_json()
    dramas.append(drama)
    return jsonify({"message": "🎉 Drama added successfully! 🎊✨", "drama": drama}), 201

# Update a drama's info
@app.route('/dramas/<name>', methods=['PUT'])
def update_drama(name):
    drama_to_update = request.get_json()
    index = get_drama_name(name, dramas)
    dramas[index] = drama_to_update
    return jsonify(dramas[index])

# Delete a drama
@app.route('/dramas/<name>', methods=['DELETE'])
def delete_drama(name):
    drama_to_delete = search_dramas(name, dramas)
    if drama_to_delete:
        dramas.remove(drama_to_delete)
        return jsonify({
            "message": f"🎉 '{name}' has been deleted successfully. 🎊✨",
            "deleted": drama_to_delete}), 200
    else:
        return jsonify({"error": f"'{name}' not found."}), 404







if __name__ == '__main__':
    app.run(debug=True)