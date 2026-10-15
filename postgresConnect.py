import psycopg2
import sys

def connectionOpen(db):
    conn_string = "host='localhost' dbname='"+db+"' user='postgres' password='Admin'"

    try:
        conn = psycopg2.connect(conn_string)

        return conn

    except Exception as e:
        raise Exception(e)    

def connectionClose(conn):
    
    conn.close()

def fetchInfo(conn, db):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM public." + db + "s")
    
    records = cursor.fetchall()
    
    print(records)
    cursor.close()
        

def postgreRead(database):

    conn = connectionOpen(database)
    fetchInfo(conn, database)

    connectionClose(conn)