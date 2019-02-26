import pandas as pd
import numpy as np
from GCForest import gcForest
from sklearn.metrics import accuracy_score
import time
from sklearn.model_selection import train_test_split

def train():
    train = pd.read_csv('train_gps.csv')
    test=pd.read_csv('test_gps.csv')
    a='row_id'
    lng='longitude'
    lat='latitude'
    drop_columns_all = 'shop_id'
    targetName = 'shop_id'
    X1 = train.drop([a,drop_columns_all,lng,lat], axis=1, inplace=False)
    X2 = test.drop([a, drop_columns_all,lng,lat], axis=1, inplace=False)
    # X1 = X1.fillna(0)
    # X2 = X2.fillna(0)
    # 先将 X1 和 Y1（DataFrame）转化成 array
    train_x = np.array(X1)
    test_x = np.array(X2)
    Y1 = list(train[targetName])
    Y11=list(set(Y1))
    print('Y1:',Y1[:5])
    list_y1={}
    for i in range(len(Y11)):
        list_y1[Y11[i]]=i
    list_key1=list(list_y1.keys())
    for j in range(len(list_key1)):
        for i in range(len(Y1)):
            if Y1[i] == list_key1[j]:
                Y1[i]=list_y1[list_key1[j]]
    # Y1 = Y1.fillna(0)
    print('Y11:', Y1[:5])
    train_y = np.array(Y1)
    Y2 = list(test[targetName])
    print('Y2:', Y2[:5])
    for j in range(len(list_key1)):
        for i in range(len(Y2)):
            if Y2[i] == list_key1[j]:
                Y2[i] = list_y1[list_key1[j]]
    # Y2 = Y2.fillna(0)
    print('Y22:', Y2[:5])
    test_y = np.array(Y2)
    # print(len(Y1),len(Y11),Y1[:2])#2638 46
    # print(len(Y2), len(Y22), Y2[:2])#560 41
    print(list_y1,'\n')
    # print(list_y2)
    # print(train_x[0],'\n')
    # print(train_y[0], '\n')
    # print(test_x[0], '\n')
    # print(test_y[0], '\n')
    # print(len(train_x),len(test_x))

train()