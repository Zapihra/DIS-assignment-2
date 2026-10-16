import psycopg2
import sys

def connectionOpen(db):
    conn_string = "host='localhost' dbname='"+db+"' user='postgres' password='password'"

    try:
        conn = psycopg2.connect(conn_string)

        return conn

    except Exception as e:
        raise Exception(e)    

def connectionClose(conn):
    
    conn.close()
    return

def fetchInfo(conn, db):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM public." + db + "s")
    
    records = cursor.fetchall()

    for record in records:
        print(record)
    cursor.close()
    return
        

def postgreRead(database):

    conn = connectionOpen(database)
    fetchInfo(conn, database)

    connectionClose(conn)
    return

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
    return

def postgreUpdate(database, info):
    conn = connectionOpen(database)
    cur = conn.cursor()

    if database == "owner":
        cur.execute("UPDATE " + database +"s SET name = (%s), email = (%s) WHERE email = (%s)", (info[1], info[2], info[0]))

    if database == "cat":
        cur.execute("UPDATE " + database +"s SET name = (%s), breed = (%s), age = (%s) WHERE name = (%s) AND age = (%s)", (info[2], info[3], info[4], info[0], info[1]))

    conn.commit()
    cur.close()
    connectionClose(conn)
    return