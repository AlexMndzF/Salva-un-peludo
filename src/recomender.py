import pandas as pd
import numpy as np
from src.photo import get_image_person
from src.NN import encoder
from src.mongo import get_image

model = encoder

def recomender(vectors,names):
    '''
    vectors = Lista de vectores de las fotos a comparar en la base de datos.
    names = Lista de los nombres de las fotos 3n la lista de vectores.
    img_path = path de la imagen a predecir.
    
    '''
    mod = list(vectors)
    s_N = names
    s = pd.Series(s_N)
    s_vector = ([mod])
    df=pd.DataFrame(s)
    df['Vector']=mod
    df.columns=(['name','X'])
    test_person=get_image_person()
    test_person_pred=model.predict(test_person)
    X_missing=test_person_pred
    df["diffs"] = df["X"].apply(lambda X: np.linalg.norm(X-X_missing))
    results = df.groupby("name").agg({'diffs':'min'}).sort_values(by='diffs')
    #display(results)
    URL, name = get_image(results.index[0])
    name = name.split('_')
    return URL, name