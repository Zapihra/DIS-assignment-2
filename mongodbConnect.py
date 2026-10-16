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


def mongodbRead():
    conn = openConnection()
    db = conn["DIS"]
    col = db["Dogs"]

    res = col.find()

    for dog in res:
        print(dog)

    closeConnection(conn)

openConnection()

def mongodbWrite(info):
    conn = openConnection()
    db = conn["DIS"]
    col = db["Dogs"]

    col.insert_one({"name": info[0], "breed": info[1], "age": info[2]})
    closeConnection(conn)
    return

def mongodbUpdate(info):
    conn = openConnection()
    db = conn["DIS"]
    col = db["Dogs"]

    col.update_one({"name": info[0], "age": info[1]}, {"$set": {"name": info[2], "breed": info[3], "age": info[4]}})

    closeConnection(conn)
    return