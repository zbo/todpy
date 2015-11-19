__author__ = 'bob.zhu'
import os
import shutil
import sys
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


def do():
    migrate_protected = ['__init__.py']
    installed_modules = ['config', 'auto', 'workspace']
    loaddata_files = ['initial_data.yaml']

    print '-' * 30 + 'remove sqlite db file'
    dbpath = os.path.join(web_path, 'db.sqlite3')
    if os.path.exists(dbpath):
        os.remove(dbpath)

    print '-' * 30 + 'copy clean sqlite db file'
    clean_dbpath = os.path.join(tests_path, 'db-init/db.sqlite3')
    shutil.copy(clean_dbpath, dbpath)

    print '-' * 30 + 'clear migrartions'
    need_clear = []
    for m in installed_modules:
        p = os.path.join(web_path, m+'/migrations/')
        for one in os.listdir(p):
            if one not in migrate_protected:
                need_clear.append(os.path.join(p, one))
    for p in need_clear:
        print '-'*30 + p + 'cleaned'
        os.remove(p)

    print '-' * 30 + 'make migrartions'

    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    execute_from_command_line(['manage.py', 'loaddata', os.path.join(web_path, 'initial_data.yaml')])



if __name__ == '__main__':
    do()
