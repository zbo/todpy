__author__ = 'bob.zhu'
import os
import sys
import django
sys.path.append('../web/web/')
sys.path.append('../web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from workspace.models import WorkSpace


class lettuce_executor:

    def __init__(self, workspace):
        self.workspace = workspace

    def runit(self):
        print "run it"

if __name__ == '__main__':
    django.setup()
    workspace = WorkSpace.objects.get(pk=3)
    print workspace
    runner = lettuce_executor(workspace)
    runner.runit()