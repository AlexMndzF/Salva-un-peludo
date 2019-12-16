import glob
import cv2
import numpy as np
from costants import BATCH_SIZE




#Funcion generadora para la NN
def createnp(path):
    print('generator initiated')
    img_data_list=[]
    count = 0
    while True:
      for img in glob.glob(path):
          input_img=cv2.imread(img)
          #input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
          input_img_resize=cv2.resize(input_img,(220,220))
          img_data_list.append(input_img_resize)
          count+=1
          if  len(img_data_list) == BATCH_SIZE:
            img_data_list = np.array(img_data_list)
            img_data_list = img_data_list.astype('float32')
            img_data_list = img_data_list/255
            yield img_data_list,img_data_list
            img_data_list = []
      if count==20500:
        break




def createtest(path,limit=1):
    '''
    Genera un numpy de las imagenes que se le pase, en caso de ser las imagenes de la base de datos genera
    tambien el nombre de las imagenes.
    '''
    img_data_list=[]
    count = 0
    names = []
    while True:
        for img in glob.glob(path):
            names.append(img.split('/')[-1].split('.')[0])
            input_img=cv2.imread(img)
            #input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            input_img_resize=cv2.resize(input_img,(220,220))
            img_data_list.append(input_img_resize)
            count+=1
            if  count == limit:
                img_data_list = np.array(img_data_list)
                img_data_list = img_data_list.astype('float32')
                img_data_list = img_data_list/255
                return img_data_list,names