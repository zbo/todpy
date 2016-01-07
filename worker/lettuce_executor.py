__author__ = 'bob.zhu'
import os
import sys
import django

sys.path.append('../web/web/')
sys.path.append('../web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from workspace.models import WorkSpace, TestLog
from config.models import FeatureLocation, AppSetting
from auto.models import Feature
import subprocess
import uuid
import pdb
import traceback

class lettuce_executor:
    def __init__(self, execution):
        self.workspace = execution.workspace
        self.execution = execution

    def runit(self):
        print "======run it======="
        project_base = AppSetting.getSetting("projectbase")[0]
        workspace_name = AppSetting.getSetting("workspace")[0]
        root_location = self.workspace.rootlocation
        entrance = self.workspace.entrance
        log_path = os.path.join(project_base, workspace_name, root_location, 'log.txt')
        if os.path.exists(log_path):
            os.remove(log_path)
        workspace_web = os.path.join(project_base, workspace_name, root_location, 'web')
        file_place = os.path.join(project_base, workspace_name, root_location, 'web/features', entrance)
        file_path = file_place + '.feature'

        cmd_gen_bin = 'cd {0} && {1} {2} --with-subunit'.format(workspace_web, 'lettuce', file_path)

        subprocess.call([cmd_gen_bin], shell=True)
        cmd_gen_sub_unit2 ='subunit2junitxml < {0}/subunit.bin'.format(workspace_web)
        process = subprocess.Popen(cmd_gen_sub_unit2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdoutput, erroutput) = process.communicate()
        log = TestLog()
        log.fill(self.execution, stdoutput, "lettuce stdout")
        log.save()
        os.remove('{0}/subunit.bin'.format(workspace_web))



        self.unlock_feature()
        print "==================="

    def unlock_feature(self):
        # pdb.set_trace()
        feature = Feature.objects.filter(workspace=self.workspace.id).first()
        feature.unlock_feature()



if __name__ == '__main__':
    django.setup()
    workspace = WorkSpace.objects.get(pk=3)
    print workspace
    runner = lettuce_executor(workspace)
    runner.runit()
