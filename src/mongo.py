from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

#Get Password
connection = os.getenv('URLMONGO')
#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db,coll=connectCollection(findyourdog, dogs)
