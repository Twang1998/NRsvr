import scipy.io as sio 
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
# #python创建一个mat文件
# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]


test_scene = ['047','005','119','023','025','013','028','053','009','108','017','044','073','056','018','115','077','118','031','001']

train_path = []
train_score = []
test_path = []
test_score = []

for i in range(120):
    if i<=99:
        scene_id = '%03d' %(i+1)
        df = pd.read_csv(os.path.join('score_and_sort/dataset_p1/score',scene_id+'_score.csv'))
        name = df['Name']
        score = df['Texture']
        if scene_id in test_scene:
            for j in range(15):
                test_path.append(os.path.join(scene_id,name[j].replace('jpg','png')))
                test_score.append([score[j]])
        else:
            for j in range(15):
                train_path.append(os.path.join(scene_id,name[j].replace('jpg','png')))
                train_score.append([score[j]])
    else:
        scene_id = '%03d' %(i+1)
        df = pd.read_csv(os.path.join('score_and_sort/dataset_p2/score','%03d' %(i+1-100)+'_score.csv'))
        name = df['Name']
        score = df['Texture']
        if scene_id in test_scene:
            for j in range(15):
                test_path.append(os.path.join(scene_id,name[j].replace('_0','_1').replace('jpg','png')))
                test_score.append([score[j]])
        else:
            for j in range(15):
                train_path.append(os.path.join(scene_id,name[j].replace('_0','_1').replace('jpg','png')))
                train_score.append([score[j]])
print(len(train_score))
print(len(test_score))
# train_score = np.array(train_score).reshape(1500,)
# test_score = np.array(test_score).reshape(300,)
# sio.savemat('train_region.mat', {'train_region_path': train_path,'train_region_score': train_score})  #变量分别保存在名字为xyz下面
# sio.savemat('test_region.mat', {'test_region_path': test_path,'test_region_score': test_score}) 