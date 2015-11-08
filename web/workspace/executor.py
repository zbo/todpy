__author__ = 'bob.zhu'
import subprocess

class Executor:
    def __init__(self):
        pass

    @staticmethod
    def execute(cmd):
        subprocess.call([cmd], shell=True)

