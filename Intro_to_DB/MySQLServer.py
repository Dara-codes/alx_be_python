from copy import error
import mysql.connector  # type: ignore

def create_database(cursor):

    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store"
        )
        print("Database 'alx_book_store' created successfully!")
    except error as e:
        print("database {e}")
        
def main():
    try:
        db = mysql.connector.connect(
            user= 'root',
            password = '1234567890123',
            host = 'alx_book_store'
        )

        cursor = db.cursor

        create_database(cursor)

        cursor.close()
        db.close()

    except error as e:
        print("couldnt connect to db due to {e}")

    else:
        db.close()
        
if __name__ == "__main__":
    main()