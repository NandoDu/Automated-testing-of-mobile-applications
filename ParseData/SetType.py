import pandas as pd
import os
import re
import cv2
import json
import numpy as np

# 设置文件目录
sourceDataPath = 'ATMobile2020-1/'
files = os.listdir(sourceDataPath)
CSVFiles = []
class_list = {}
index_list = {}
# 将CSV文件的文件名按大小顺序存入CSV文件列表
for file in files:
    if re.match('.*\\.csv', file):
        csv_file = file.split('.')[0]
        CSVFiles.append(int(csv_file))
CSVFiles.sort()
# 将所有CSV文件中所有行对应的class加入到class_list中，并累计每个class对应的次数
for i in range(len(CSVFiles)):
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    for k in range(len(csv_file)):
        class_name = csv_file.iloc[k]['class'].split('.')[-1]
        if class_name in class_list.keys():
            class_list[class_name] = class_list[class_name] + 1
        else:
            class_list[class_name] = 1
            index_list[class_name] = str(i)
    # print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 打印所有的class名
print('*******************')
print('类别')
print('*******************')
for key in class_list.keys():
    print(index_list[key] + ' : ' + key + ' --- ' + str(class_list[key]))
print('*******************')
