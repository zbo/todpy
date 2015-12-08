__author__ = 'bob.zhu'

protected = ['01','02']
import shutil
import os, sys
current_dir = path = sys.path[0]
path_len= current_dir.index('todpy')+len('todpy')
root_path=current_dir[:path_len]
web_path=os.path.join(root_path,'web')
tests_path=os.path.join(root_path,'tests')
web_web_path=os.path.join(root_path,'web/web')
unittests_path=os.path.join(root_path,'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.management import execute_from_command_line
folder = os.path.join(root_path,'workspaces')

def do():
    print '-'*30+'before clear there are:'
    listdir = os.listdir(folder)
    print listdir
    print '-'*30+'perform clear actions:'
    for d in listdir:
        if d in protected:
            continue
        print '-'*20+'clear: '+d
        dir_path = os.path.join(folder, d)
        if os.path.isfile(dir_path):
            continue
        shutil.rmtree(dir_path)
    print '-'*30+'after clear there are:'
    print os.listdir(folder)
    print '='*20+'some folders protected are:'
    print protected

if __name__ == '__main__':
    do()
