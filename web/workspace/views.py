from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from auto.models import Feature
from models import WorkSpace, Execution, TestLog
import sys,os
import json
import pdb
import base64
import xml.etree.ElementTree
from django.views.decorators.csrf import csrf_exempt
import csv


def get_web_path():
    current_dir = path = sys.path[0]
    path_len= current_dir.index('todpy')+len('todpy')
    root_path=current_dir[:path_len]
    return root_path


def read_log(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    workspace = WorkSpace.objects.get(pk=workspace_id)
    path = get_web_path()
    log_path = os.path.join(path,'workspaces', workspace.rootlocation,'log.txt')
    f = open(log_path, 'r')
    content =f.readlines()
    f.close()
    return HttpResponse(content)


def read_screenshot(request, feature_id):
    # pdb.set_trace()
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    workspace = WorkSpace.objects.get(pk=workspace_id)
    path = get_web_path()
    screenshot_path = os.path.join(path,'workspaces', workspace.rootlocation, 'web', 'logs', 'screenshot.png')
    with open(screenshot_path, "rb") as image_file:
        content = base64.b64encode(image_file.read())
        image_file.close()
        return HttpResponse(content)


@csrf_exempt
def get_screenshot_by_path(request):
    try:
        json_data = request.body
        # pdb.set_trace()
        obj = json.loads(json_data)
        feature_id = obj['featureId']
        feature = Feature.objects.get(pk=feature_id)
        workspace_id = feature.workspace
        workspace = WorkSpace.objects.get(pk=workspace_id)
        path = get_web_path()
        screenshot_path = os.path.join(path, 'workspaces', workspace.rootlocation, 'web', obj['path'])
        with open(screenshot_path, "rb") as image_file:
            content = base64.b64encode(image_file.read())
            image_file.close()
            return HttpResponse(content)

    except Exception, e:
        return HttpResponse(content="screenshot not exist", content_type=None, status=500, reason="file error");


def read_screenshot_index(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    workspace = WorkSpace.objects.get(pk=workspace_id)
    path = get_web_path()

    _history = []
    # try:
    #     _history = request.session.__getitem__("_build_index")
    #     _index = _history[(_history.__len__()-1)] if _history.__len__() > 1 else {"directory": "0", "id": "0", "pass": 0,
    #                                                                               "failure": 0, "error": 0, "total": "0"}
    # except KeyError,e:

    index_path = os.path.join(path, 'workspaces', workspace.rootlocation, 'web', 'index.csv')
    _index = {}
    with open(index_path, 'rb') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',', quotechar='|')
        for row in csv_reader:
            _history.append(row)
            _index = row
        request.session.__setitem__("_build_index", _history)

    index_path = os.path.join(path, 'workspaces', workspace.rootlocation, 'web', 'logs', _index["directory"], 'index.xml')
    # index_xml = xml.etree.ElementTree.parse(index_path).getroot()
    f = open(index_path, "r")
    content = f.readlines()
    f.close()
    return HttpResponse(content)


def read_building_screenshot(request, feature_id):

    pass


def read_build_history(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    workspace = WorkSpace.objects.get(pk=workspace_id)
    path = get_web_path()

    index_path = os.path.join(path, 'workspaces', workspace.rootlocation, 'web', 'index.csv')
    # pdb.set_trace()
    results = []
    with open(index_path, 'rb') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',', quotechar='|')
        for row in csv_reader:
            results.append(row)
        request.session.__setitem__("_build_index", results)
    return HttpResponse(json.dumps(results))


def read_console(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    execution = Execution.objects.filter(workspace_id=workspace_id).order_by('starttime').last()
    testlog = execution.testlog_set.first()
    return HttpResponse(testlog.content)