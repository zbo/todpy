__author__ = 'bob.zhu'
import pdb
import time


def logit(func):
    def wrapper(*args):
        write_file(
            "{0} start @ {1}".format(func.func_name, time.strftime('%Y-%m-%d %X %Z', time.localtime(time.time()))))
        func(*args)
        write_file(
            "{0} end @ {1}".format(func.func_name, time.strftime('%Y-%m-%d %X %Z', time.localtime(time.time()))))

    return wrapper


def write_file(content):
    file_object = open("./save.txt", "a")
    file_object.writelines(content + "\r\n")
    file_object.close()
    pass