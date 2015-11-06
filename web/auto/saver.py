__author__ = 'bob.zhu'
import json
from models import Feature, Scenario, Step


class StepDtoPostSaver:
    def __init__(self):
        pass

    def replace_u(self, str_in):
        tmp = '['
        for s in str_in:
            tmp += s + ','
        return tmp[0:len(tmp) - 1] + ']'

    def save(self, json_str):
        json_obj = json.loads(json_str)
        feature_name = json_obj['feature']['feature_name']
        feature_desc = json_obj['feature']['feature_description']
        feature_save = Feature().fill(feature_name, feature_desc, '', '')
        feature_save.save()
        scenarios = json_obj['feature']['scenarios']

        for sce in scenarios:
            sequence = ''
            sce_save = Scenario().fill(feature_save, sce['scenario_name'], '')
            sce_save.save()
            steps = sce['steps']
            for step in steps:
                step = step[step.keys()[0]]
                step_save = Step().fill(sce_save, step['step_name'], step['co_name'], step['co_file_name'],
                                        step['co_firstlineno'], step['co_argcount'],
                                        self.replace_u(step['co_varnames']))
                step_save.save()
                sequence += str(step_save.id) + '|'
            sce_save.set_sequence(sequence)
            sce_save.save()
        return feature_save
