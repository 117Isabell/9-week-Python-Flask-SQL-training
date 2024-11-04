## What is this repo for:
<p align="left">All the assignments for the 9-week training </p>


# Assignment Four: K-Dramas Management API

## Requirements

Before running the API, ensure you have the following installed:

- Python 3.x
- Flask
- MySQL Connector for Python
- Requests

You can install the required packages using pip. Create a `requirements.txt` file with the following content:

```plaintext
Flask
mysql-connector-python
requests
```

Then run:

```shellscript
pip install -r requirements.txt
```

## Configuring Database Connection

You need to edit the `db_config.py` file to set up your database connection parameters. Create a file named `db_config.py` and define the following variables:

```python
USER = 'your_database_username'
PASSWORD = 'your_database_password'
HOST = 'localhost'  # or your database host
DB_NAME = 'dramas'   # the name of your database
```

Replace `your_database_username`, `your_database_password`, and other details with your actual database credentials.

## Running the API

1. Start the Flask application: Navigate to the directory where your `app.py` file is located, then run the following command:

```shellscript
python app.py
```

This will start the Flask server, and you should see output indicating that the server is running, typically at `http://127.0.0.1:5000/`.


2. Testing the API: You can test the API using tools like Postman or directly through the command line using curl or by running the `main.py` script that provides a command-line interface to interact with the API.


## Endpoints

### GET /

Returns a greeting message.

Response Example:

```json
{
    "Greeting": "Hello, you are finally here!"
}
```

### GET /dramas

Returns all dramas in the database.

Response Example:

```json
[
    {
        "Name": "The Bridal Mask",
        "Year of release": "2012",
        ...
    },
    ...
]
```

### GET /dramas/`<name>`

Searches for a drama by name.

Response Example:

```json
{
    "Name": "The Bridal Mask",
    "Year of release": "2012",
    ...
}
```

Error Response (if not found):

```json
{
    "error": "😞 Drama not found! 🚫"
}
```

### POST /dramas

Adds a new drama.

Request Body Example:

```json
{
    "Name": "The Bridal Mask",
    "Year of release": "2012",
    ...
}
```

Response Example:

```json
{
    "message": "🎉 Drama added successfully! 🎊✨",
    "drama": {
        ...
    }
}
```

### PUT /dramas/`<name>`

Updates an existing drama's information.

Request Body Example:

```json
{
    "New content": "🎉 The information has been updated successfully",
    "Rating": "9.5"
}
```

Response Example:

```json
{
    "Name": "The Bridal Mask",
    "Year of release": "2012",
    ...
}
```

### DELETE /dramas/`<name>`

Deletes a drama by name.

Response Example:

```json
{
    "message": "🎉 'The Bridal Mask' has been deleted successfully. 🎊✨",
    "deleted": {
        ...
    }
}
```

Error Response (if not found):

```json
{
    "error": "'The Bridal Mask' not found."
}
```

## Conclusion
You should now have a K-Dramas Management API set up and ready to use. Have fun!


### Additional Notes:

- Make sure to customize the `db_config.py` and any other configuration files according to your setup.
- Ensure your database schema matches the expected structure used in your queries.
- You can test the endpoints using tools like Postman or directly in your `main.py`.


   
<br><br>
# Assignment Three
## A video demon of the project-Play with Pokemon API to fetch some Poké data, like names and heights
Check out the demo video: [Watch on YouTube](https://youtu.be/3kUayEoKSg4)

## Run on Your Local Machine 

1. Clone that repo locally:
2. Open the project in PyCharm
3. Install Dependencies
4. Navigate to the root Directory
5. Run the project locally:
   ```bash
   python3 pokemon.py
   ```
6. Open in a Browser:
   <p>Once the server is running, open your web browser and navigate to the local link provided in the terminal (usually http://127.0.0.1:5000).
</p>

<h4>Inspirations</h4>
1. My old Pokemon API project in JS: https://github.com/117Isabell/pokedex_projects 
2. This Python flask tutorial: https://www.youtube.com/watch?v=dam0GPOAvVI

<h4>Extra info about Flask</h4>
<p>Flask is a micro web framework written in Python. <br>
For more details, please go to: https://flask.palletsprojects.com/en/3.0.x/# 
</p>


<br><br>

## Assignment Two

<h1 align="left">Week One Notes:</h1>

<p align="left">Session 3--Clone a repo and connect remote and local repo:</p>

If making a repository locally - start from:

1. If cloning a repository, `git clone repository`, ensure you have the main (default branch) changes pulled, and then continue from step 3.
2. If you have a repository already connected/setup on GitHub, replace step 1 with checking out main (`git checkout origin main`) and pulling the changes (`git pull`).

Steps:

1. `git init`
2. `git checkout -b new_branch_name` <- to work on a branch (we did not cover this today though)
3. Make your changes, add files, edit code, etc.
4. When you wish to save, add your files to the staging area (bank of things to be committed) using `git add .` (or `git add filename`)
5. `git commit -m "meaningful commit message"`
6. `git push`
7. If you don't have a branch set up on the remote yet (we didn't cover branches today), it will tell you what code to run (e.g., `git push --set-upstream origin branch_name`)
8. Repeat from step 3 until you're complete (you'll look at when to move onto a new branch, and what they are in more detail, later)

<p align="left">Session 4--Create and switch branches, push local changes and create pull requests:</p>

1. Make a repo on GitHub (including the readme file option and make sure it's private).
2. Clone that repo locally:
3. Make a branch:
   ```bash
   git switch name-of-branch
   ```
4. Make the changes locally:
   ```bash
   git add .
   git commit -m "description of the changes you made!"
   git push
   ```



<br><br>


<h5 align="left">Let's connect:</h5>
<p align="left">
<a href="https://www.linkedin.com/in/peifang-luo-dev/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="peifang(isabell) luo" height="30" width="40" /></a>
</p>
