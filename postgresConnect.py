import psycopg2
import sys

def connectionOpen():
    conn_string = "host='localhost' dbname='assignment2' user='postgres' password='Admin'"

    conn = psycopg2.connect(conn_string)

    return conn

def connectionClose(conn):
    
    conn.close()

def fetchInfo(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    
    records = cursor.fetchall()
    
    print(records)
    cursor.close()
        

def postgreConnection():
    conn = connectionOpen()

    fetchInfo(conn)

    connectionClose(conn)