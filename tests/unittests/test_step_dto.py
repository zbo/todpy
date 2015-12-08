__author__ = 'bob.zhu'
import sys
import os
import django
import json

current_dir = path = sys.path[0]
path_len= current_dir.index('todpy')+len('todpy')
root_path=current_dir[:path_len]
web_path=os.path.join(root_path,'web')
web_web_path=os.path.join(root_path,'web/web')
tests_path=os.path.join(root_path,'tests')
unittests_path=os.path.join(root_path,'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
workspace_path = os.path.join(root_path, 'workspaces')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
from config.models import AppSetting, FeatureLocation
from workspace.models import WorkSpace
from auto.generator import FeatureFileGenerator



class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, StepDto):
            return obj.render_json()
        return json.JSONEncoder.default(self, obj)


def load_config():
    global config
    config = {}
    for setting in AppSetting.objects.all():
        config[setting.type] = setting.value


def test():
    django.setup()
    load_config()
    feature_id = 1
    file_path = os.path.join(workspace_path,'01')
    result = {}
    dict = Step.getStepByFolder(file_path)
    keys = dict.keys()
    temp = {}
    for key in keys:
        step_dto = StepDto()
        step_dto.co_filename = dict[key].func_code.co_filename
        step_dto.co_firstlineno = dict[key].func_code.co_firstlineno
        step_dto.co_argcount = dict[key].func_code.co_argcount
        step_dto.co_varnames = dict[key].func_code.co_varnames
        step_dto.co_name = dict[key].func_code.co_name
        temp[key] = step_dto
    result = result.copy()
    result.update(temp)
    #print result
    #print json.dumps(result, cls=DateEncoder)
    #print '=' * 80
    return result


if __name__ == '__main__':
    test()
