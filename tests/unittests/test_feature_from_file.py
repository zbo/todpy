__author__ = 'bob.zhu'
import os
import shutil
import sys

current_dir = path = sys.path[0]
path_len = current_dir.index('todpy') + len('todpy')
root_path = current_dir[:path_len]
web_path = os.path.join(root_path, 'web')
tests_path = os.path.join(root_path, 'tests')
web_web_path = os.path.join(root_path, 'web/web')
workspace_path = os.path.join(root_path, 'workspaces')
unittests_path = os.path.join(root_path, 'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.management import execute_from_command_line


def test():
    file_path = os.path.join(workspace_path, '01', 'features', 'testcase.feature')
    file_obj = open(file_path)
    print file_obj.readlines()
    file_obj.close()
    pass


if __name__ == '__main__':
    test()
