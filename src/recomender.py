import pandas as pd
import numpy as np
from photo_transform import createtest
from NN import encoder

def recomender(vectors,names,img_path):
    '''
    test = Lista de vectores de las fotos a comparar en la base de datos.
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
    test_person=createtest(img_path)
    test_person_pred=encoder.predict(test_person[0]) #hay que coger el elemento 0 por que la fincion esta preparada para cargar mas imagenes y devuelve lista convertida a np.
    X_missing=test_person_pred
    df["diffs"] = df["X"].apply(lambda X: np.linalg.norm(X-X_missing))
    results = df.groupby("name").agg({'diffs':'min'}).sort_values(by='diffs')
    return results.index[0]
