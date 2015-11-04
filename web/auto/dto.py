__author__ = 'bob.zhu'
import json


class DateEncoder(json.JSONEncoder):
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

    def render_json(self):
        json = {}
        json['co_file_name'] = self.co_filename
        json['co_firstlineno'] = self.co_firstlineno
        json['co_argcount'] = self.co_argcount
        json['co_varnames'] = self.co_varnames
        json['co_name'] = self.co_name
        json['step_name'] = self.step_name
        return json

class StepDtoPostConvert:
    def convert(self):

        pass
