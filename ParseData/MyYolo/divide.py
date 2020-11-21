import os
import random

# 训练集和测试集按9:1划分
trainval_percent = 0.1
train_percent = 0.9
# 加载标注文件目录
labelfilepath = 'Annotations'
# 加载存取训练划分策略的目录
txtsavepath = 'ImageSets\Main'
total_label = os.listdir(labelfilepath)
# 随机划分标注文件集
num = len(total_label)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')
# 写入记录训练文件位置的文件、记录测试文件位置的文件和记录验证文件位置的文件
for i in list:
    name = total_label[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
