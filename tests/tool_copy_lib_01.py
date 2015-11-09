__author__ = 'bob.zhu'
import os
import shutil

web_lib= '../libraries/web'
workspace_floder = '../workspaces/01/'
def do():
    print '-'*30+'start move libraries from web:'
    print os.listdir(web_lib)
    shutil.rmtree(workspace_floder)
    shutil.copytree(web_lib,workspace_floder)

if __name__ == '__main__':
    do()