# -*- coding: utf-8 -*-
import os
import re
import json
import cv2
import pandas as pd

# 设置文件存储目录
sourceDataPath = 'ATMobile2020-1/'
files = os.listdir(sourceDataPath)
# 将JSON文件的文件名按大小顺序存入JSON文件列表
JSONFiles = []
for file in files:
    if re.match('.*\\.json', file):
        json_file = file.split('.')[0]
        JSONFiles.append(int(json_file))
JSONFiles.sort()
# 将JPG文件的文件名按大小顺序存入JPG文件列表
JPGFiles = []
for file in files:
    if re.match('.*\\.jpg', file):
        jpg_file = file.split('.')[0]
        JPGFiles.append(int(jpg_file))
JPGFiles.sort()
# 将JSON文件批量转为CSV文件
for i in range(len(JSONFiles)):
    json_file = str(JSONFiles[i]) + '.json'
    json_obj = open(sourceDataPath + json_file)
    json_data = json.load(json_obj)
    # 存取所有控件的坐标的列表
    coordinates = []
    # 存取所有控件的列表
    widgets = []
    fields = []
    # 按JSON文件中的字段新建数据表
    dataFrame = pd.DataFrame(columns=['scrollable-horizontal',
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

    # 根据JSON特点递归存取控件和控件坐标
    def getCoordinate(tempObj, father):
        # 清除无效的控件信息
        if tempObj is not None:
            # 存取每个控件的父控件
            tempObj['father'] = father
            coordinates.append(tempObj['bounds'])
            if "children" in tempObj:
                searchList = tempObj['children']
                # 标注控件存在子控件
                tempObj['children'] = True
                widgets.append(tempObj)
                for child in searchList:
                    getCoordinate(child, tempObj['pointer'])
            else:
                tempObj['children'] = False
                widgets.append(tempObj)

    # 清除无效的JSON文件
    if json_data['activity']['root'] is None:
        continue
    getCoordinate(json_data['activity']['root'], "")
    image = cv2.imread(sourceDataPath + str(JPGFiles[0]) + '.jpg')
    x, y = image.shape[0:2]
    # 根据图片尺寸特点，调整尺寸
    image = cv2.resize(image, (int(y / 3), int(x / 3)))
    # print()
    # print('*******************')
    # print('图像尺寸为：' + str(int(y / 3)) + ' X ' + str(int(x / 3)))
    # print('*******************')
    # print()
    cnt = 0
    monitor_pool = []
    for k in range(len(widgets)):
        monitor_pool.append(k)
    # for i in monitor_pool:
    #     coordinate = coordinates[i]
    #     cnt = cnt + 1
    #     first_point = (int(coordinate[0] / 4), int(coordinate[1] / 4))
    #     last_point = (int(coordinate[2] / 4), int(coordinate[3] / 4))
    #     center_point = (int((coordinate[0] / 4 + coordinate[2] / 4) / 2), int((coordinate[1] / 4 + coordinate[3] / 4) / 2))
    #     image = cv2.rectangle(image, first_point, last_point, (0, 255, 0), 2)
    #     image = cv2.putText(image, str(i), (first_point[0] + 10, first_point[1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        # image = cv2.line(image, first_point, (first_point[0] + 10, first_point[1] + 10), (255, 255, 0), 2)
    cnt = 0
    # 循环存取控件信息到CSV表
    for k in monitor_pool:
        widget = widgets[k]
        cnt = cnt + 1
        # print('第' + str(i) + '个控件的信息如下：')
        # print('*******************')
        # print('图像尺寸为：' + str(int(coordinates[i][2] / 4 - coordinates[i][0] / 4)) + ' X ' + str(int(coordinates[i][3] / 4 - coordinates[i][1] / 4)))
        # print('*******************')
        # print(json.dumps(widget, indent=4))
        # print()
        # 填充CSV表的各个字段
        for key in widget.keys():
            dataFrame.loc[k, key] = widget[key]
            if key in fields:
                pass
            else:
                fields.append(key)
    dataFrame.to_csv(sourceDataPath + str(JSONFiles[i]) + '.csv', index=False)
    # print('*******************')
    # print('数据库字段')
    # print('*******************')
    # for field in fields:
    #     print(field)
    # print('*******************')
    # print(dataFrame)
    # cv2.namedWindow('IMG', cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('IMG', image)
    # cv2.waitKey(0)
    print('已完成' + str((i / len(JSONFiles)) * 100) + '%')

