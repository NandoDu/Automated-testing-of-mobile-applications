import os
import pandas as pd
import re

# 设置15个类别
classes = ['Button',
           'Text',
           'Advertisement',
           'MenuItem',
           'Calendar',
           'Video',
           'ProgressBar',
           'Image',
           'Chart',
           'CheckBox',
           'Switch',
           'Edit',
           'SeekBar',
           'Dialog',
           'ToolBarItem']


# 将控件的原始坐标转化为用于yolov3训练的坐标
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


# 生成标注文件
def convert_annotation(image_id):
    in_file = open(sourceDataPath + '%s.csv' % image_id)
    out_file = open('Annotations/%s.txt' % image_id, 'w')
    csv_content = pd.read_csv(in_file)
    w = 1080
    h = 1920
    for i in range(len(csv_content)):
        cls = csv_content.iloc[i]['type']
        cls_id = classes.index(cls)
        csvbox = eval(csv_content.iloc[i]['bounds'])
        b = (float(csvbox[0] * 3 / 4), float(csvbox[2] * 3 / 4), float(csvbox[1] * 3 / 4), float(csvbox[3] * 3 / 4))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == '__main__':
    # 设置文件目录
    sourceDataPath = '/Users/goduchuanqi/Desktop/自动化测试大作业/GUI/ATMobile2020-1/'
    files = os.listdir(sourceDataPath)
    # 将CSV文件的文件名按大小顺序存入CSV文件列表
    CSVFiles = []
    for file in files:
        if re.match('.*\\.csv', file):
            csv_file = file.split('.')[0]
            CSVFiles.append(int(csv_file))
    CSVFiles.sort()
    # 对每一个CSV文件进行处理，得到记录坐标和类别的标注文件
    for i in range(len(CSVFiles)):
        csv_file = CSVFiles[i]
        convert_annotation(csv_file)
        print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
