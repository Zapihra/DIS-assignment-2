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

def postgreWrite(database, info):
    conn = connectionOpen(database)
    cur = conn.cursor()
    
    if database == "owner":
        cur.execute("INSERT INTO " + database + "s VALUES (%s, %s)", (info[0],info[1]))

    elif database == "cat":
        cur.execute("INSERT INTO " + database + "s VALUES (%s, %s, %s)", (info[0],info[1], info[2]))

    conn.commit()
    cur.close()
    connectionClose(conn)