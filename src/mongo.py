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

db,coll=connectCollection('findyourdog', 'dogs')


def mongo_add(documents):
    '''
    documents: list of dicts to ad to the db
    '''
    for i in range(len(documents)):
        coll.insert_one(documents[i])
    
def get_image(recomend_name):
    image = list(coll.find({'name':f'{recomend_name}'}))[0].get('url')
    name = list(coll.find({'name':f'{recomend_name}'}))[0].get('name')
    return image,name