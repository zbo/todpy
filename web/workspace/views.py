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
        return HttpResponse(content="screenshot not exist",content_type=None, status=500, reason="file error");


def read_screenshot_index(request, feature_id):
    # pdb.set_trace()
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    workspace = WorkSpace.objects.get(pk=workspace_id)
    path = get_web_path()
    index_path = os.path.join(path,'workspaces', workspace.rootlocation, 'web', 'logs', feature.name, 'index.xml')
    # index_xml = xml.etree.ElementTree.parse(index_path).getroot()
    f = open(index_path,"r")
    content = f.readlines()
    f.close()
    return HttpResponse(content)



def read_console(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    execution = Execution.objects.filter(workspace_id=workspace_id).order_by('starttime').last()
    testlog = execution.testlog_set.first()
    return HttpResponse(testlog.content)