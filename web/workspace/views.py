from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from auto.models import Feature
from models import WorkSpace, Execution, TestLog
import sys,os
import pdb

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

def read_console(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    execution = Execution.objects.filter(workspace_id=workspace_id).order_by('starttime').last()
    testlog = execution.testlog_set.first()
    return HttpResponse(testlog.content)