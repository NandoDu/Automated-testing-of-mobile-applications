import pandas as pd
import os
import re
import numpy as np

# 设置文件目录
sourceDataPath = 'ATMobile2020-1/'
files = os.listdir(sourceDataPath)
CSVFiles = []
class_list = []
# 将CSV文件的文件名按大小顺序存入CSV文件列表
for file in files:
    if re.match('.*\\.csv', file):
        csv_file = file.split('.')[0]
        CSVFiles.append(int(csv_file))
CSVFiles.sort()
# 删除type为0的行
for i in range(len(CSVFiles)):
    filter_csv_file = pd.DataFrame(columns=['scrollable-horizontal',
                                            'draw',
                                            'clickable',
                                            'pressed',
                                            'focusable',
                                            'long-clickable',
                                            'enabled',
                                            'bounds',
                                            'visibility',
                                            'focused',
                                            'selected',
                                            'scrollable-vertical',
                                            'children',
                                            'adapter-view',
                                            'abs-pos',
                                            'pointer',
                                            'class',
                                            'visible-to-user',
                                            'father',
                                            'text',
                                            'type'])
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    pointer = 0
    for k in range(len(csv_file)):
        if pd.isnull(csv_file.iloc[k]['type']):
            continue
        filter_csv_file.loc[pointer] = csv_file.iloc[k]
        pointer = pointer + 1
    filter_csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除有子控件的行、对用户不可见的控件的行以及不可见的控件的行
for i in range(len(CSVFiles)):
    filter_csv_file = pd.DataFrame(columns=['scrollable-horizontal',
                                            'draw',
                                            'clickable',
                                            'pressed',
                                            'focusable',
                                            'long-clickable',
                                            'enabled',
                                            'bounds',
                                            'visibility',
                                            'focused',
                                            'selected',
                                            'scrollable-vertical',
                                            'children',
                                            'adapter-view',
                                            'abs-pos',
                                            'pointer',
                                            'class',
                                            'visible-to-user',
                                            'father',
                                            'text'])
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    pointer = 0
    for k in range(len(csv_file)):
        if csv_file.iloc[k]['children']:
            continue
        if not csv_file.iloc[k]['visible-to-user']:
            continue
        if not csv_file.iloc[k]['visibility']:
            continue
        filter_csv_file.loc[pointer] = csv_file.iloc[k]
        pointer = pointer + 1
    filter_csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除class字段中包含"DecorView"的行
for i in range(len(CSVFiles)):
    filter_csv_file = pd.DataFrame(columns=['scrollable-horizontal',
                                            'draw',
                                            'clickable',
                                            'pressed',
                                            'focusable',
                                            'long-clickable',
                                            'enabled',
                                            'bounds',
                                            'visibility',
                                            'focused',
                                            'selected',
                                            'scrollable-vertical',
                                            'children',
                                            'adapter-view',
                                            'abs-pos',
                                            'pointer',
                                            'class',
                                            'visible-to-user',
                                            'father',
                                            'text'])
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    pointer = 0
    for k in range(len(csv_file)):
        class_name = csv_file.iloc[k]['class']
        if 'DecorView' in class_name:
            continue
        else:
            filter_csv_file.loc[pointer] = csv_file.iloc[k]
            pointer = pointer + 1
    filter_csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除class字段为"android.view.View"的行
for i in range(len(CSVFiles)):
    filter_csv_file = pd.DataFrame(columns=['scrollable-horizontal',
                                            'draw',
                                            'ancestors',
                                            'clickable',
                                            'pressed',
                                            'focusable',
                                            'long-clickable',
                                            'enabled',
                                            'bounds',
                                            'visibility',
                                            'content-desc',
                                            'rel-bounds',
                                            'focused',
                                            'selected',
                                            'scrollable-vertical',
                                            'children',
                                            'adapter-view',
                                            'abs-pos',
                                            'pointer',
                                            'class',
                                            'visible-to-user',
                                            'father',
                                            'resource-id',
                                            'package',
                                            'text',
                                            'font-family'])
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    pointer = 0
    for k in range(len(csv_file)):
        class_name = csv_file.iloc[k]['class']
        if class_name == 'android.view.View':
            continue
        else:
            filter_csv_file.loc[pointer] = csv_file.iloc[k]
            pointer = pointer + 1
    filter_csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除class字段包含"layout"的行
for i in range(len(CSVFiles)):
    filter_csv_file = pd.DataFrame(columns=['scrollable-horizontal',
                                            'draw',
                                            'ancestors',
                                            'clickable',
                                            'pressed',
                                            'focusable',
                                            'long-clickable',
                                            'enabled',
                                            'bounds',
                                            'visibility',
                                            'content-desc',
                                            'rel-bounds',
                                            'focused',
                                            'selected',
                                            'scrollable-vertical',
                                            'children',
                                            'adapter-view',
                                            'abs-pos',
                                            'pointer',
                                            'class',
                                            'visible-to-user',
                                            'father',
                                            'resource-id',
                                            'package',
                                            'text',
                                            'font-family'])
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    pointer = 0
    for k in range(len(csv_file)):
        class_name = (csv_file.iloc[k]['class']).lower()
        if 'layout' in class_name:
            continue
        else:
            filter_csv_file.loc[pointer] = csv_file.iloc[k]
            pointer = pointer + 1
    filter_csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除长为0或宽为0的字段
for i in range(len(CSVFiles)):
    filter_csv_file = pd.DataFrame(columns=['scrollable-horizontal',
                                            'draw',
                                            'ancestors',
                                            'clickable',
                                            'pressed',
                                            'focusable',
                                            'long-clickable',
                                            'enabled',
                                            'bounds',
                                            'visibility',
                                            'content-desc',
                                            'rel-bounds',
                                            'focused',
                                            'selected',
                                            'scrollable-vertical',
                                            'children',
                                            'adapter-view',
                                            'abs-pos',
                                            'pointer',
                                            'class',
                                            'visible-to-user',
                                            'father',
                                            'resource-id',
                                            'package',
                                            'text',
                                            'font-family'])
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    baseLen = len(csv_file)
    pointer = 0
    for k in range(len(csv_file)):
        bounds = eval(csv_file.iloc[k]['bounds'])
        if bounds[2] - bounds[0] == 0 or bounds[3] - bounds[1] == 0:
            continue
        else:
            filter_csv_file.loc[pointer] = csv_file.iloc[k]
            pointer = pointer + 1
    filter_csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除无用的font-family字段
for i in range(len(CSVFiles)):
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    csv_file.drop(['font-family'], axis=1, inplace=True)
    csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除无用的content-desc字段
for i in range(len(CSVFiles)):
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    csv_file.drop(['content-desc'], axis=1, inplace=True)
    csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除无用的ancestors、rel-bounds、resource-id、package字段
for i in range(len(CSVFiles)):
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    csv_file.drop(['ancestors', 'rel-bounds', 'resource-id', 'package'], axis=1, inplace=True)
    csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 删除坐标重复的字段
for i in range(len(CSVFiles)):
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    csv_file.drop_duplicates(subset=['bounds'], keep='last', inplace=True)
    csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# 打印所有的class名
# for i in range(len(CSVFiles)):
#     csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
#     for k in range(len(csv_file)):
#         if csv_file.iloc[k]['class'] in class_list:
#             pass
#         else:
#             class_list.append(csv_file.iloc[k]['class'])
#     print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
# print('*******************')
# print('类别')
# print('*******************')
# for class_name in class_list:
#     print(class_name)
# for i in range(len(CSVFiles)):
#     csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
#     csv_file['type'] = ''
#     csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
#     print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
