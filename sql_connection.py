import mysql.connector
from config import USER, PASSWORD, HOST, DB_NAME

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

def get_all_dramas():
    try:
        db_name = 'dramas'  # update as required
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM k_dramas"""
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")









def main():
    get_all_dramas()



if __name__ == '__main__':
    main()