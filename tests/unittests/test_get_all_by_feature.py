__author__ = 'bob.zhu'
import sys
import os
import django
import lettuce
import json
import uuid
import unittest

current_dir = path = sys.path[0]
path_len = current_dir.index('todpy') + len('todpy')
root_path = current_dir[:path_len]
web_path = os.path.join(root_path, 'web')
web_web_path = os.path.join(root_path, 'web/web')
tests_path = os.path.join(root_path, 'tests')
unittests_path = os.path.join(root_path, 'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
workspace_path = os.path.join(root_path, 'workspaces')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto, FeatureDto, ScenarioDto, DataEncoder
from workspace.models import WorkSpace
from auto.generator import FeatureFileGenerator
import re

compiled_regx = {}


def match_definision(step_item, source_dict):
    for patten in source_dict.keys():
        if not compiled_regx.get(patten):
            compiled_regx[patten] = re.compile(patten)
        prog = compiled_regx.get(patten)
        result = prog.search(step_item.original_sentence)
        if result:
            return source_dict.get(patten), patten, result
    return None


def extract_func_info(co_func, s_item, result):
    action_type = result.string[0:result.regs[0][0] - 1].strip()
    varlist_tuple = co_func.func_code.co_varnames
    variables = []
    for var in result.regs[1:]:
        variables.append(result.string[var[0]:var[1]])
    return action_type, varlist_tuple, variables


def test():
    django.setup()
    feature_id = 1
    feature = Feature.objects.filter(id=feature_id).first()
    workspace = WorkSpace.objects.get(pk=feature.workspace)
    workspace_path = workspace.getFolderPath()
    dict = Step.getStepByFolder(workspace_path)
    file_path = FeatureFileGenerator.get_workspace_entrance(workspace)
    feature = lettuce.Feature.from_file(file_path)
    feature_dto = FeatureDto(feature.name, feature.description)
    scenarios = []
    for sce in feature.scenarios:
        s_dto = ScenarioDto('id_missing', sce.name)
        for s_item in sce.steps:
            co_func, patten, result = match_definision(s_item, dict)
            action_type, varlist_tuple, variables = extract_func_info(co_func, s_item, result)
            step_dto = StepDto()
            func_code = co_func.func_code
            step_dto.fill(func_code.co_filename, func_code.co_firstlineno, func_code.co_argcount,
                          varlist_tuple, func_code.co_name, co_func.func_name, action_type, variables, patten,
                          'id_no_use')
            s_dto.steps.append(step_dto)
        scenarios.append(s_dto)
    feature_dto.fill_scenarios(scenarios)
    return json.dumps((feature_dto), cls=DataEncoder)


if __name__ == '__main__':
    test()
    # self.id=id
