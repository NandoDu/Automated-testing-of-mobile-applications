import os

# 读取存取测试文件路径的文件，此处以我用于测试的文件为例
with open("darknet/build/darknet/x64/data/test.txt", "r") as testTXTFilesPath:
    testTXTFiles = testTXTFilesPath.readlines()
# 更改当前工作目录
os.chdir("darknet/build/darknet/x64/")
# 批量检测测试文件
for testTXTFile in testTXTFiles:
    # 由于模型大小大于100M，从百度云下载后放入darknet/build/darknet/x64/backup目录中才可运行
    os.system("darknet.exe detector test data/obj.data yolo-obj.cfg backup/yolo-obj_last.weights %s" % testTXTFile)
    # 更改输出图片和描述文件的文件名
    try:
        os.rename("output/predictions.jpg", "output/" + testTXTFile.split('/')[-1][0:-1])
        os.rename("output/description.txt", "output/" + testTXTFile.split('/')[-1][0:-5] + '.txt')
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
    else:
        print('rename file success\r\n')
