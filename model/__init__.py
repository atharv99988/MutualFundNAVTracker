import mysql.connector 
from mysql.connector import Error

def connect() :
    try:
        # Step 3: Create a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',        # Database host
            database='mutualfunds', # Database name
            user='root',     # Database user
            password='root@123'  # User's password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection

    except Error as e:
        print(f"Error: {e}")