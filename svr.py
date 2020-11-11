import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import scipy.io as sio 
from scipy import stats

train_global = sio.loadmat('train_region.mat')
train_path = train_global['train_region_path']
train_score = train_global['train_region_score'].reshape(1500,)
# print(train_score.shape)

test_global = sio.loadmat('test_region.mat')
test_path = test_global['test_region_path']
test_score = test_global['test_region_score'].reshape(300,)

### 这里修改不同方法提取的特征
train_feature = sio.loadmat('NR/BRISQUE/train_region_feature.mat')['result']
# print(train_feature['result'].shape)   ## (1500,36)
# print(a)
test_feature = sio.loadmat('NR/BRISQUE/test_region_feature.mat')['result2']



clf = SVR(kernel='rbf', C=1.0)
# x_tran,x_test,y_train,y_test = train_test_split(x, y, test_size=0.25)
clf.fit(train_feature, train_score)
pre_test_score = clf.predict(test_feature)

## 计算传统算法的srcc和plcc
all_srcc = []
all_plcc = []
for i in range(20):
    gt_scores = test_score[i*15:(i+1)*15]
    pred_scores = pre_test_score[i*15:(i+1)*15]

    srcc, _ = stats.spearmanr(pred_scores, gt_scores)
    plcc, _ = stats.pearsonr(pred_scores, gt_scores)

    all_srcc.append(srcc)
    all_plcc.append(plcc)
mean_srcc = np.mean(all_srcc)
mean_plcc = np.mean(all_plcc)
print(all_srcc)
print(mean_srcc)
print(mean_plcc)
## 计算传统算法的两两比较准确率
acc = []
for i in range(20):
    gt_scores = test_score[i*15:(i+1)*15]
    pred_scores = pre_test_score[i*15:(i+1)*15]
    total = 0
    num = 0
    for j in range(15-1):
        for k in range(j+1,15):
            total +=1
            if(gt_scores[j] >= gt_scores[k] and pred_scores[j] >= pred_scores[k]) or (gt_scores[j] < gt_scores[k] and pred_scores[j] < pred_scores[k]):
                num += 1
            else:
                pass
    # print(total)
    single_acc = num/total
    acc.append(single_acc)
mean_acc = np.mean(acc)

print(acc)
print(mean_acc)

