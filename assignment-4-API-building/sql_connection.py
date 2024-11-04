"""
This Python provides functions to connect to a MySQL database and perform CRUD operations on a 'k_dramas' table,
including fetching all dramas, getting dramas above a certain rating, and adding new dramas.

Make sure to customize the db_config.py and any other configuration files according to your setup.
Ensure your database schema matches the expected structure used in your queries
and you can run the sql script file in the assignment-4-sql_scripts folder in MySQL workbench to set up a db and a table.

Functions:
- get_all_dramas(): Fetches and prints all dramas from the database.
- get_dramas_above_rating(rating_score): Fetches and prints dramas with a rating above the specified score.
- add_drama(drama): Adds a new drama to the database.
"""

import mysql.connector
from db_config import USER, PASSWORD, HOST, DB_NAME

class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DB_NAME
    )
    return cnx

# Get all the dramas
def get_all_dramas():
    db_connection = None
    try:
        db_name = 'dramas'  # update to match with your db name
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("🎉✨Connected to DB: %s " % db_name)

        query = """SELECT * FROM k_dramas"""
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)
        cur.close()
    except Exception:
        raise DbConnectionError("😞Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("🎉✨DB connection is closed")
            print()

# Get all the dramas which rated over a certain score
def get_dramas_above_rating(rating_score):
    db_connection = None
    try:
        db_name = 'dramas'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("🎉✨Connected to DB: %s" % DB_NAME)

        query = """SELECT * FROM k_dramas WHERE rating > %s"""
        cur.execute(query, (rating_score,))
        result = cur.fetchall()
        drama_count = len(result)
        print(f"🎉✨ The total count of dramas with rating above {rating_score} is: {drama_count}")
        for drama in result:
            print(drama)
        cur.close()
        return drama_count

    except Exception as e:
        print(e)
        raise DbConnectionError("😞Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("🎉✨DB connection is closed")

def add_drama(drama):
    db_connection = None
    try:
        db_name = 'dramas'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("🎉✨Connected to DB: %s" % DB_NAME)

        query = """
            INSERT INTO k_dramas (name, year_of_release, aired_date, aired_on, number_of_episodes, network, duration, content_rating, synopsis, cast, genre, tags, `rank`, rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Prepare the data for insertion
        data = (
            drama.get('name'),
            drama.get('year_of_release'),
            drama.get('aired_date'),
            drama.get('aired_on'),
            drama.get('number_of_episodes'),
            drama.get('network'),
            drama.get('duration'),
            drama.get('content_rating'),
            drama.get('synopsis'),
            drama.get('cast'),
            drama.get('genre'),
            drama.get('tags'),
            drama.get('rank'),
            drama.get('rating')
        )

        # Execute the query
        cur.execute(query, data)
        db_connection.commit()
        print(f"🎉 Drama '{drama['name']}' added successfully! 🎊✨")
        cur.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise DbConnectionError("Failed to insert data into DB")
    finally:
        if db_connection:
            db_connection.close()
            print("🎉✨DB connection is closed")


def main():
    get_all_dramas()

    # An example of getting all dramas rating over 9
    rating_score = 9
    get_dramas_above_rating(rating_score)
    print()

    # Drama to be added
    new_drama = {
        "name": "The Bridal Mask",
        "year_of_release": "2012",
        "aired_date": "May 30, 2012 - Sep  6, 2012",
        "aired_on": "Wednesday, Thursday",
        "number_of_episodes": 28,
        "network": "KBS2",
        "duration": "1 hr. 5 min.",
        "content_rating": "15+ - Teens 15 or older",
        "synopsis": "Lee Kang To is an ambitious and callous Korean officer employed by the Japanese colonists. Despite his mother's disapproval of his work and his own brother's antagonistic history with the Japanese, Kang To continues to play by the colonist's rules in hopes of becoming successful and bringing his family out of poverty. However, a mysterious figure wearing a traditional Bridal Mask always seems to get in Kang To's way. The Bridal Mask appears as a Zorro-like figure who protects the people from the Japanese colonists' oppression and abuse of power. An unexpected turn of events brings Kang To to cross paths with the mysterious Bridal Mask, changing his future and the nation's history forever.",
        "cast": "Joo Won, Jin Se Yeon, Park Ki Woong, Han Chae Ah, Shin Hyun Joon, Chun Ho Jin",
        "genre": "Action, Historical, Romance, Political",
        "tags": "Japanese Colonial Rule, Hidden Identity, Rebellion, Revenge, Love Triangle, Murder, First Love, Adapted From A Manhwa, Investigation, Drama",
        "rank": "#99",
        "rating": 8.6
    }
    add_drama(new_drama)


if __name__ == '__main__':
    main()