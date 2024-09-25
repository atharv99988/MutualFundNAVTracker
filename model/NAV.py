from model import connect
from mysql.connector import Error

def insertNAV(mutualFundId, NAV, growth) :
    insert_query = """INSERT INTO navs (mutualfundid, NAV, navgrowth, createuser, lastmoduser) VALUES (%s, %s, %s, %s, %s)"""
    connection = connect()
    try:
        if  connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(insert_query, (mutualFundId, NAV, growth, 'atharv','atharv'))
            connection.commit()
    except Error as e :
        print(f"Error: {e}")
    finally:    
        cursor.close()
        connection.close()