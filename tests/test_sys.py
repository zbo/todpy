__author__ = 'bob.zhu'
import os
import shutil

folder_path = './test-folder'

file_path = folder_path + '/' + 'test.txt'

def add_file(p):
    f = open(p, 'w')
    f.close()


def check_file_exist(path):
    if os.path.exists(path):
        return True
    return False


def create_folder(file_path):
    os.makedirs(file_path)


def remove_file(file_path):
    os.remove(file_path)

def remove_folder(folder_path):
    shutil.rmtree(folder_path)

if check_file_exist(folder_path) == False:
    create_folder(folder_path)
    print '='*10+'create folder'+'='*10

if check_file_exist(file_path) == False:
    add_file(file_path)
    print '='*10+'create file'+'='*10

remove_file(file_path)
print '='*10+'remove file'+'='*10
remove_folder(folder_path)
print '='*10+'remove folder'+'='*10