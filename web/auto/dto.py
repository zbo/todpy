__author__ = 'bob.zhu'
import json


class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, StepDto):
            return obj.render_json()
        return json.JSONEncoder.default(self, obj)


class StepDto:
    def __init__(self):
        self.uuid = ''
        self.co_filename = ''
        self.co_firstlineno = 0
        self.co_argcount = 0
        self.co_varnames = {}
        self.co_name = ''
        self.step_name = ''
        self.parameters = []

    def fill(self, co_file_name, co_firstlineno, co_argcount, co_varnames, co_name, step_name):
        self.co_filename = co_file_name
        self.co_firstlineno = co_firstlineno
        self.co_argcount = co_argcount
        self.co_varnames = co_varnames
        self.co_name = co_name
        self.step_name = step_name

    def render_json(self):
        json = {}
        json['co_file_name'] = self.co_filename
        json['co_firstlineno'] = self.co_firstlineno
        json['co_argcount'] = self.co_argcount
        json['co_varnames'] = self.co_varnames
        json['co_name'] = self.co_name
        json['step_name'] = self.step_name
        return json


class FeatureDto:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.scenarios = []

    def fill_scenarios(self, scenario_list):
        for sce in scenario_list:
            self.scenarios.append(sce)


class ScenarioDto:
    def __init__(self, description):
        self.description = description
        self.steps = []

    def fill_steps(self, step_set):
        for step in step_set.all():
            s_dto = StepDto()
            # s_dto.fill(step.module,step.location,)
            # self.steps.append(s)
