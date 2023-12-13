import random
import os

a = list(range(0,4788))
origin = list(range(0,4788))
random.shuffle(a)


train_len = (len(a)*70//100)

train_set = a[:train_len]
val_set = a[train_len:]

root = '../../dataset/kitti/ImageSets/'

with open(root+'trainval.txt','w') as trainval:
    for idx, i in enumerate(origin):
        if idx+1 < len(origin):
            trainval.write('{:06d}'.format(origin[idx])+'\n')
        else:
            trainval.write('{:06d}'.format(origin[idx]))

with open(root+'train.txt','w') as train:
    for idx, i in enumerate(train_set):
        if idx+1 < len(train_set):
            train.write('{:06d}'.format(train_set[idx])+'\n')
        else:
            train.write('{:06d}'.format(train_set[idx]))

with open(root+'val.txt','w') as val:
    for idx, i in enumerate(val_set):
        if idx+1 < len(val_set):
            val.write('{:06d}'.format(val_set[idx])+'\n')
        else:
            val.write('{:06d}'.format(val_set[idx]))
