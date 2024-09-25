from model import connect
from mysql.connector import Error

def insertMutualFund(name,URL):
    if name != '' and URL != '' :    #later add more validations
        insert_query = """INSERT INTO mutualfunds (name, url, createuser, lastmoduser) VALUES (%s, %s, %s, %s)"""
        connection = connect()
        try:
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(insert_query, (name,URL,'atharv','atharv'))
                connection.commit()
                cursor.close()
                connection.close()
        except Error as e :
            print(f"Error: {e}")



def getMutualFund() :
    query = """SELECT MutualFundId, URL FROM mutualfunds.mutualfunds"""
    connection = connect()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            print(rows)
            cursor.close()
            connection.close()
            return rows
    except Error as e :
        print(f"Error: {e}")

