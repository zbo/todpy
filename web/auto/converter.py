__author__ = 'bob.zhu'
import json
from models import Feature, Scenario, Step


class StepDtoPostConvert:
    def __init__(self):
        pass

    def convert(self, json_str):
        json_obj = json.loads(json_str)
        feature_name = json_obj['feature']['feature_name']
        feature_save = Feature().fill(feature_name, '', '')
        feature_save.save()
        scenarios = json_obj['feature']['scenarios']
        for sce in scenarios:
            sce_save = Scenario().fill(feature_save, sce['scenario_name'], '')
            sce_save.save()
            steps = sce['steps']
            for step in steps:
                step = step[step.keys()[0]]
                step_save = Step().fill(sce_save, step['step_name'], step['co_name'], step['co_file_name'],
                                        step['co_firstlineno'])
                step_save.save()
        return feature_save
