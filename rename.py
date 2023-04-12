# 读取所有文件名
import os
import re
import random

path = './dataset'
# 读取文件名
def get_file_name(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(file)
    return file_list

# 打乱并重命名
def rename(path):
    file_list = get_file_name(path)
    random.shuffle(file_list)
    for i in range(len(file_list)):
        os.rename(os.path.join(path, file_list[i]), os.path.join(path, str(i) + '.jpg'))

if __name__ == '__main__':
    rename(path)