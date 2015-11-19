__author__ = 'bob.zhu'
import json
import pdb
import models

class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, StepDto):
            return obj.render_json()
        if isinstance(obj, FeatureDto):
            return obj.render_json()
        return json.JSONEncoder.default(self, obj)


class StepDto:
    def __init__(self):
        self.uuid = ''
        self.id=''
        self.co_filename = ''
        self.co_firstlineno = 0
        self.co_argcount = 0
        self.co_varnames = {}
        self.co_name = ''
        self.step_name = ''
        self.co_variables = []
        self.action_type = ''
        self.description = ''

    def fill(self, co_file_name, co_firstlineno, co_argcount, co_varnames, co_name, step_name, action_type, co_variables, description, id):
        self.co_filename = co_file_name
        self.co_firstlineno = co_firstlineno
        self.co_argcount = co_argcount
        self.co_varnames = co_varnames
        self.co_name = co_name
        self.step_name = step_name
        self.action_type = action_type
        self.co_variables = co_variables
        self.description = description
        self.id=id

    def render_json(self):
        json_ret = {}
        json_ret['co_file_name'] = self.co_filename
        json_ret['co_firstlineno'] = self.co_firstlineno
        json_ret['co_argcount'] = self.co_argcount
        json_ret['co_varnames'] = self.co_varnames
        json_ret['co_name'] = self.co_name
        json_ret['step_name'] = self.step_name
        json_ret['action_type'] = self.action_type
        json_ret['co_variables'] = self.co_variables
        json_ret['description'] = self.description
        if hasattr(self, "id"):
            json_ret['id'] = self.id
        
        return json_ret


class FeatureDto:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.scenarios = []

    def set_id(self, id):
        self.id = id

    def fill_scenarios(self, scenario_list):
        for sce in scenario_list:
            self.scenarios.append(sce)

    def render_json(self):
        json = {}
        if hasattr(self, 'id'):
            json['id']=self.id

        json['name'] = self.name
        json['description'] = self.description
        scenarios = []
        for sce in self.scenarios:
            scenarios.append(sce.render_json())
        json['scenarios'] = scenarios
        return json


class ScenarioDto:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.steps = []

    def fill_steps(self, scenario):
        sequence = scenario.step_sequence
        sequence = sequence[0:len(sequence)-1]
        sequence_array = sequence.split('|')
        for id in sequence_array:
            step = models.Step.objects.get(pk=id)
            s_dto = StepDto()
            s_dto.fill(step.module,step.location, step.argnumbers, step.varlist, step.function, step.description,step.action_type, step.co_variables, step.description_with_agrs, id)
            self.steps.append(s_dto)

    def render_json(self):
        json={}
        json['id'] = self.id
        json['description'] = self.description
        steps = []
        for step in self.steps:
            steps.append(step.render_json())
        json['steps']=steps
        return json
