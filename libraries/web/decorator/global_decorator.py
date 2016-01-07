__author__ = 'bob.zhu'
import pdb
import time
import traceback
from lettuce import *
from selenium import webdriver
import os

def logit(func):
    def wrapper(*args):
        # pdb.set_trace()
        write_file(
            "{0} start @ {1}".format(func.func_name, time.strftime('%Y-%m-%d %X %Z', time.localtime(time.time()))))
        try:
            func(*args)
            save_snapshot(args[0], func.func_name)
        except Exception, e:
            write_file(traceback.format_exc())
            # pdb.set_trace()
            _step = args[0]
            _flag = False
            _screenshot = os.path.join(world.scenario_root, "error.png")
            world.browser.get_screenshot_as_file(_screenshot)
            try:
                index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
                for s in _step.scenario.steps:
                    if not s.passed:
                        errorLog = "" if _flag else traceback.format_exc()
                        fail_step = "<step name=\""+\
                                    s.__dict__.get('original_sentence')+"\" pass=\"false\" >"+errorLog+"</step>\r\n"
                        index_file.writelines(fail_step)
                        _flag=True
            finally:
                index_file.close()

            # _line_no = _step.__dict__.get('described_at').__dict__.get('line')
            # _screenshot = str(_line_no)+"_"+func.func_name+".png"

            # binary_screenshot = world.browser.get_screenshot_as_base64()

            world.browser.close()
            raise e
        write_file(
            "{0} end @ {1}".format(func.func_name, time.strftime('%Y-%m-%d %X %Z', time.localtime(time.time()))))
    return wrapper


def write_file(content):
    file_object = open("../log.txt", "a")
    file_object.writelines(content + "\r\n")
    file_object.close()
    pass


def save_snapshot(_step, _func_name):
    _line_no = _step.__dict__.get('described_at').__dict__.get('line')
    _image_name = str(_line_no)+"_"+_func_name+".png"
    try:
        world.browser.get_screenshot_as_file(os.path.join(world.scenario_root, _image_name))
        index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
        step_info = "<step name=\""+_step.__dict__.get('original_sentence')+"\" img=\""+_image_name+"\" pass=\"true\"></step>\r\n"
        index_file.writelines(step_info)
    except Exception, e:
        index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
        step_info = "<step name=\""+_step.__dict__.get('original_sentence')+"\" pass=\"true\"></step>\r\n"
        index_file.writelines(step_info)

    finally:
        index_file.close()

    pass
