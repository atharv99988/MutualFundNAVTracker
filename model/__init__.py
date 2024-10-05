import mysql.connector 
from mysql.connector import Error
from .config import DataBaseConfig

def connect() :
    try:
        # Step 3: Create a connection to the MySQL database
        connection = mysql.connector.connect(
            host = DataBaseConfig.host,        # Database host
            database = DataBaseConfig.database, # Database name
            user = DataBaseConfig.user,     # Database user
            password = DataBaseConfig.password  # User's password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection

    except Error as e:
        print(f"Error: {e}")