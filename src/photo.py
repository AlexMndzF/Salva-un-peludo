import glob
import cv2
import numpy as np
from src.costants import BATCH_SIZE
from flask import request
import os


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




def createtest(path):
    '''
    Create a numpy array, returns the np and a list of list:
    list name,ext
    '''
    img_data_list=[]
    count = 0
    names = []
    while True:
        for img in glob.glob(path):
            names.append(img.split('/')[-1].split('.'))
            input_img=cv2.imread(img)
            #input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            input_img_resize=cv2.resize(input_img,(220,220))
            img_data_list.append(input_img_resize)
            count+=1
        img_data_list = np.array(img_data_list)
        img_data_list = img_data_list.astype('float32')
        img_data_list = img_data_list/255
        return img_data_list,names

def uploadimg():
    upload    = request.files.get('upload')
    print('==============>UPLOAD',upload.filename)
    if upload == None or upload.filename == '':
        return 'Error no image'
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'Error'
    upload.save('test/upload.png') # appends upload.filename automatically
    return f'test/upload.png'

def get_image_person(path='test/upload.png'):
    #print('-------------->>>>___',path)
    img_data_list=[]
    input_img=cv2.imread(path)
    #print(input_img)
    input_img_resize=cv2.resize(input_img,(220,220))
    img_data_list.append(input_img_resize)
    img_data_list = np.array(img_data_list)
    img_data_list = img_data_list.astype('float32')
    img_data_list = img_data_list/255
    return img_data_list