import pandas as pd
import os
import re
import numpy as np

# 设置文件目录
sourceDataPath = 'ATMobile2020-1/'
files = os.listdir(sourceDataPath)
CSVFiles = []
class_list = []
total_widget = 0
marked_widget = 0
# 将CSV文件的文件名按大小顺序存入CSV文件列表
for file in files:
    if re.match('.*\\.csv', file):
        csv_file = file.split('.')[0]
        CSVFiles.append(int(csv_file))
CSVFiles.sort()
# 循环读取每一个CSV文件
for i in range(len(CSVFiles)):
    csv_file = pd.read_csv(sourceDataPath + str(CSVFiles[i]) + '.csv')
    # 对每一个CSV文件中的控件进行类型判别
    for k in range(len(csv_file)):
        # 获取class字段以'.'做分割的最后一段字符串
        class_name = ((csv_file.iloc[k]['class']).lower()).split('.')[-1]
        total_widget = total_widget + 1
        # 标注过类别的行直接跳过
        if not pd.isnull(csv_file.iloc[k]['type']):
            marked_widget = marked_widget + 1
            continue
        # class_name包含button的优先判定为Button
        if 'button' in class_name:
            csv_file.loc[k, 'type'] = 'Button'
            continue
        # class_name包含chart的判定为Chart，优先级大于Image
        if 'chart' in class_name:
            csv_file.loc[k, 'type'] = 'Chart'
            continue
        # class_name包含menu的判定为MenuItem，优先级大于Image
        if 'menu' in class_name:
            csv_file.loc[k, 'type'] = 'MenuItem'
            continue
        # class_name包含dialog的判定为Dialog
        if 'dialog' in class_name:
            csv_file.loc[k, 'type'] = 'Dialog'
            continue
        # class_name包含Calendar或month的判定为Calendar
        if 'calendar' in class_name or 'month' in class_name:
            csv_file.loc[k, 'type'] = 'Calendar'
            continue
        # class_name包含video的判定为Video
        if 'video' in class_name:
            csv_file.loc[k, 'type'] = 'Video'
            continue
        # class_name包含progress的判定为ProgressBar
        if 'progress' in class_name:
            csv_file.loc[k, 'type'] = 'ProgressBar'
            continue
        # class_name包含check的判定为CheckBox
        if 'check' in class_name:
            csv_file.loc[k, 'type'] = 'CheckBox'
            continue
        # class_name包含switch的判定为Switch
        if 'switch' in class_name:
            csv_file.loc[k, 'type'] = 'Switch'
            continue
        # class_name包含seek的判定为SeekBar
        if 'seek' in class_name:
            csv_file.loc[k, 'type'] = 'SeekBar'
            continue
        # class_name包含o的判定为Advertisement
        if class_name == 'o':
            csv_file.loc[k, 'type'] = 'Advertisement'
            continue
        # class_name包含tool的判定为ToolBarItem
        if 'tool' in class_name:
            csv_file.loc[k, 'type'] = 'ToolBarItem'
            continue
        # class_name包含image的判定为Image
        if 'image' in class_name:
            csv_file.loc[k, 'type'] = 'Image'
            continue
        # class_name包含edit的判定为Edit
        if 'edit' in class_name:
            csv_file.loc[k, 'type'] = 'Edit'
            continue
        # class_name包含text的判定为Text
        if 'text' in class_name:
            csv_file.loc[k, 'type'] = 'Text'
            continue
        # 可点击并且可聚焦的统一判定为Button
        if csv_file.iloc[k]['clickable'] == True and csv_file.iloc[k]['focusable'] == True:
            csv_file.loc[k, 'type'] = 'Button'
            continue
        # text字段不为空的统一判定为Text
        if not pd.isnull(csv_file.iloc[k]['text']):
            csv_file.loc[k, 'type'] = 'Text'
            continue
    csv_file.to_csv(sourceDataPath + str(CSVFiles[i]) + '.csv', index=False)
    print('已完成' + str((i / len(CSVFiles)) * 100) + '%')
print()
print('*******************')
print('控件总数：' + str(total_widget))
print('已标注：' + str(marked_widget))
print('*******************')
