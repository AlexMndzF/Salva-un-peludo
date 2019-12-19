import pymongo
from src.photo import createtest
from src.NN import encoder 
import numpy as np
from src.mongo import coll
from src.cloudinary_api import uploadfoto_cloudinary
import glob
import os

model = encoder

def load_database(path):
    vector,names = createtest(path+'*')
    vector = model.predict(vector)
    list_db = []
    for i in range(len(names)):
        print(names[i])
        name = names[i][0]
        ext = names[i][1]
        uploadfoto_cloudinary(name,path+name+f'.{ext}')
        new_dog = {
            'name':names[i][0],
            'vector':vector[i].tolist(), #To list serialize the array to deserialize: np.array(vector)
            'url':f'https://res.cloudinary.com/alexmendezf/image/upload/v1576579565/final_database/{name}.{ext}'
        }
        list_db.append(new_dog)
    return list_db

def get_vectors_names(): 
    '''
    data: busqueda en la base de datos transformada a lista
    '''
    data = list(coll.find({}))
    vector = []
    names = []
    for i in range(len(data)):
        names.append(data[i].get('name'))
        vector.append(np.array(data[i].get('vector')))
    return vector, names

def cleandir(path):    
    files = glob.glob(path)
    for f in files:
        os.remove(f)