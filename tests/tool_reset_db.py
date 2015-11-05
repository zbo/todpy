__author__ = 'bob.zhu'
import os
import shutil

migrate_protected = ['__init__.py']
installed_modules = ['config', 'auto', 'workspace']
loaddata_files = ['initial_data.yaml']

print '-' * 30 + 'remove sqlite db file'
dbpath = '../web/db.sqlite3'
if os.path.exists(dbpath):
    os.remove(dbpath)

print '-' * 30 + 'copy clean sqlite db file'
clean_dbpath = 'db-init/db.sqlite3'
shutil.copy(clean_dbpath, dbpath)

print '-' * 30 + 'clear migrartions'
need_clear = []
for m in installed_modules:
    p = '../web/'+m+'/migrations/'
    for one in os.listdir(p):
        if one not in migrate_protected:
            need_clear.append(p+one)
for p in need_clear:
    print '-'*30 + p + 'cleaned'
    os.remove(p)

print '-' * 30 + 'make migrartions'
os.system('python ../web/manage.py makemigrations')

print '-' * 30 + 'execute migrartions'
os.system('python ../web/manage.py migrate')

print '-' * 30 + 'execute loaddata'
os.system('cd ../web && python manage.py loaddata initial_data.yaml')