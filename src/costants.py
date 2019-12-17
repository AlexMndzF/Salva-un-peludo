BATCH_SIZE = 100
EPOCH = 5

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


import os
import glob
count = 0
for e in glob.glob('Dogs/*/*'):
  count+=1
print(count)
IMG_NUM=count