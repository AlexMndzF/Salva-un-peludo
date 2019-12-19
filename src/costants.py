BATCH_SIZE = 100
EPOCH = 5

import os
import glob
count = 0
for e in glob.glob('Dogs/*/*'):
  count+=1
print(count)
IMG_NUM=count