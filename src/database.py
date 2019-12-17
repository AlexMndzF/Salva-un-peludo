import pymongo
from src.photo import createtest
from src.NN import model




def load_database(path,limit):
    vector,names = createtest(path,limit)
    vector = model.predict(vector)
    list_db = []
    for i in range(len(names)):
        print(names[i])
        new_dog = {
            'name':names[i],
            'vector':vector[i].tolist(), #To list serialize the array to deserialize: np.array(vector)
            'url':f'https://res.cloudinary.com/alexmendezf/image/upload/v1576579565/final_database/{names[i]}.jpg'
        }
        list_db.append(new_dog)
    return list_db