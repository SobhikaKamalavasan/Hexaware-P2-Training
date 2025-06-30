import mysql.connector

def getConnection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dharshini2004",
        database="carrental",
        port=3306
    )
    return connection
