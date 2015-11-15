__author__ = 'bob.zhu'
import os
import sys
import django
sys.path.append('../web/web/')
sys.path.append('../web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from workspace.models import WorkSpace
from config.models import FeatureLocation, AppSetting


class lettuce_executor:

    def __init__(self, workspace):
        self.workspace = workspace

    def runit(self):
        print "======run it======="
        project_base = AppSetting.getSetting("projectbase")[0]
        workspace_name = AppSetting.getSetting("workspace")[0]
        root_location = self.workspace.rootlocation
        entrance = self.workspace.entrance
        file_place = os.path.join(project_base,workspace_name,root_location,'web/features',entrance)
        file_path = file_place+'.feature'
        print file_path
        print "==================="

if __name__ == '__main__':
    django.setup()
    workspace = WorkSpace.objects.get(pk=3)
    print workspace
    runner = lettuce_executor(workspace)
    runner.runit()