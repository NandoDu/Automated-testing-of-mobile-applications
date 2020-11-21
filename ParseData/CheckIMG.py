import pandas as pd
import os
import re
import cv2
import json
import numpy as np

# 设置检测的文件的序号
check_index = 60
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
# 将JPG文件的文件名按大小顺序存入JPG文件列表
JPGFiles = []
for file in files:
    if re.match('.*\\.jpg', file):
        jpg_file = file.split('.')[0]
        JPGFiles.append(int(jpg_file))
JPGFiles.sort()
# 将JSON文件的文件名按大小顺序存入JSON文件列表
JSONFiles = []
for file in files:
    if re.match('.*\\.json', file):
        json_file = file.split('.')[0]
        JSONFiles.append(int(json_file))
JSONFiles.sort()
# 按检测序号加载csv文件
csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[check_index]) + '.csv')
csv_file = pd.read_csv(sourceDataPath + "28409" + '.csv')
# 按检测序号加载jpg文件
image = cv2.imread(sourceDataPath + str(JPGFiles[check_index]) + '.jpg')
image = cv2.imread(sourceDataPath + "28409" + '.jpg')
x, y = image.shape[0:2]
# 调整图片尺寸
image = cv2.resize(image, (int(y / 3), int(x / 3)))
coordinates = []
print(str(JPGFiles[check_index]) + '.jpg')
print(str(CSVFiles[check_index]) + '.csv')
print(str(JSONFiles[check_index]) + '.json')
# 打印原始JSON文件信息
json_file = str(JSONFiles[check_index]) + '.json'
json_file = "28409" + '.json'
json_obj = open(sourceDataPath + json_file)
json_data = json.load(json_obj)
print(json.dumps(json_data, indent=4))
# i = 9
# coordinate = eval(csv_file.iloc[i]['bounds'])
# first_point = (int(coordinate[0] / 4), int(coordinate[1] / 4))
# last_point = (int(coordinate[2] / 4), int(coordinate[3] / 4))
# image = cv2.putText(image, str(i), (first_point[0], first_point[1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
# image = cv2.rectangle(image, first_point, last_point, (0, 255, 0), 2)
# print(csv_file.iloc[i]['class'])
# print(csv_file.iloc[i]['bounds'])
# 打印每个控件对应的矩形框
for i in range(len(csv_file)):
    # if i != 3:
    #     continue
    coordinate = eval(csv_file.iloc[i]['bounds'])
    class_name = csv_file.iloc[i]['class']
    type = csv_file.iloc[i]['type']
    first_point = (int(coordinate[0] / 4), int(coordinate[1] / 4))
    last_point = (int(coordinate[2] / 4), int(coordinate[3] / 4))
    image = cv2.putText(image, type, (first_point[0] + 3, first_point[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    image = cv2.rectangle(image, first_point, last_point, (0, 255, 0), 2)
    print(i, eval(csv_file.iloc[i]['bounds']), csv_file.iloc[i]['class'])
cv2.namedWindow('IMG', cv2.WINDOW_AUTOSIZE)
cv2.imshow('IMG', image)
cv2.waitKey(0)
