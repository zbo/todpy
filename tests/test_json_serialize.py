__author__ = 'bob.zhu'
from datetime import datetime
import json


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


json_1 = {'num': 1112, 'date': datetime.now()}
print json.dumps(json_1, cls=DateEncoder)

print '-' * 120


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
obj = json.loads(json_str)
print obj

print '-' * 120

open_step_str = '''{"I input text into textbox with id '([^']*)'":
                    {"co_firstlineno": 7, "co_name": "i_type_text",
                    "step_name": "I input text into textbox with id '([^']*)'",
                    "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_edit.py",
                    "co_varnames": ["step", "id", "element"]},

                    "I see the '([^']*)' in the title":
                    {"co_firstlineno": 11, "co_name": "then_i_see_the_group1_in_the_title",
                    "step_name": "I see the '([^']*)' in the title", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/assert/web_see.py",
                    "co_varnames": ["step", "text"]},

                    "I open page '([^']*)'":
                    {"co_firstlineno": 13, "co_name": "i_open_page",
                    "step_name": "I open page '([^']*)'", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                    "co_varnames": ["step", "url"]},

                    "I click element with text '([^']*)'":
                    {"co_firstlineno": 14, "co_name": "i_click_element_with_text",
                    "step_name": "I click element with text '([^']*)'", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                    "co_varnames": ["step", "text", "element"]},

                    "I close web browser":
                    {"co_firstlineno": 18, "co_name": "i_close_browser",
                    "step_name": "I close web browser", "co_argcount": 1,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                    "co_varnames": ["step"]},

                    "I open web browser":
                    {"co_firstlineno": 8, "co_name": "i_open_browser",
                    "step_name": "I open web browser", "co_argcount": 1,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                    "co_varnames": ["step"]},

                    "I record log '([^']*)'":
                    {"co_firstlineno": 7, "co_name": "i_record_log", "step_name": "I record log '([^']*)'", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_log.py",
                    "co_varnames": ["step", "message"]},

                    "I click element with class '([^']*)'":
                    {"co_firstlineno": 7, "co_name": "i_click_element_with_class", "step_name": "I click element with class '([^']*)'", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                    "co_varnames": ["step", "css", "element"]}}'''

all_steps = json.loads(open_step_str)
print all_steps

print '-' * 120
three_steps = '''[
                {
                    "id-0001":
                    {"co_firstlineno": 8, "co_name": "i_open_browser",
                    "step_name": "I open web browser", "co_argcount": 1,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                    "co_varnames": ["step"]}
                },
                {   "id-0002":
                    {"co_firstlineno": 13, "co_name": "i_open_page",
                    "step_name": "I open page '([^']*)'", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                    "co_varnames": ["step", "url"]}
                },
                {
                    "id-0003":
                    {"co_firstlineno": 14, "co_name": "i_click_element_with_text",
                    "step_name": "I click element with text '([^']*)'", "co_argcount": 2,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                    "co_varnames": ["step", "text", "element"]}
                },
                {
                    "id-0004":
                    {"co_firstlineno": 18, "co_name": "i_close_browser",
                    "step_name": "I close web browser", "co_argcount": 1,
                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                    "co_varnames": ["step"]}
                }
            ]'''
three_steps = json.loads(three_steps)
print len(three_steps)
