from pymongo import MongoClient

def openConnection():

    try: 
        uri = "mongodb://localhost:27017/"
        client  = MongoClient(uri)
        
        return client


    except Exception as e:
        raise Exception(e)


def closeConnection(conn):

    conn.close()


def mongodbConnection():
    conn = openConnection()
    db = conn["DIS"]
    col = db["Dogs"]

    res = col.find_one({"name": "Musti"})

    print(res)

    closeConnection(conn)

openConnection()