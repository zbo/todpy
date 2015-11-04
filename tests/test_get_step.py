__author__ = 'bob.zhu'

import sys
import lettuce

sys.path.append('../')
from steploader import load_steps


def printArray(array):
    for item in array:
        print item


def print_reg(modules):
    global i
    for i in range(len(modules)):
        print '<---------------------------------------->'
        printArray(modules[i].STEP_REGISTRY.keys())

def clear_global(moudles):
    for m in moudles:
        m.STEP_REGISTRY.clear()
        m.CALLBACK_REGISTRY.clear()


base_path = '../simple-selenium'
android_path = '../libraries/android'

modules_android = load_steps(android_path)
print len(modules_android)
print_reg(modules_android)
#clear_global(modules_android)

modules_basic = load_steps(base_path)
print len(modules_basic)
print_reg(modules_basic)
#clear_global(modules_basic)

