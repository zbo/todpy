__author__ = 'bob.zhu'
folder = '../workspaces/'
protected = ['01','02']
import shutil
import os

print '-'*30+'before clear there are:'
listdir = os.listdir(folder)
print listdir
print '-'*30+'perform clear actions:'
for d in listdir:
    if d in protected:
        continue
    print '-'*20+'clear: '+d
    shutil.rmtree(folder+d)
print '-'*30+'after clear there are:'
print os.listdir(folder)
print '='*20+'some folders protected are:'
print protected
