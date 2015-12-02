import sys

sys.path.append('../')
sys.path.append('../../')
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Feature, Scenario, Step
from workspace.models import WorkSpace
from dto import DataEncoder, StepDto, FeatureDto, ScenarioDto
from django.views.decorators.csrf import csrf_exempt
from auto.saver import StepDtoPostSaver, StepDtoPostUpdater
from workspace.saver import WorkSpaceGenerater, ExecutionPlanSaver
from auto.generator import FeatureFileGenerator
import json
import lettuce
import re
import pdb

compiled_regx = {}


def match_definision(step_item, source_dict):
    for patten in source_dict.keys():
        if not compiled_regx.get(patten):
            compiled_regx[patten] = re.compile(patten)
        prog = compiled_regx.get(patten)
        result = prog.search(step_item.original_sentence)
        if result:
            return source_dict.get(patten), patten, result
    return None


def extract_func_info(co_func, s_item, result):
    action_type = result.string[0:result.regs[0][0] - 1].strip()
    varlist_tuple = co_func.func_code.co_varnames
    variables = []
    for var in result.regs[1:]:
        variables.append(result.string[var[0]:var[1]])
    return action_type, varlist_tuple, variables


def index(request):
    steps = Step.getStepByFolder('../simple-selenium')
    return render(request, 'auto/index.html', {'steps': steps})


def create(request):
    return render(request, 'auto/create.html')


# http://localhost:8000/auto/search_steps?key_word=aaa&type=ios
def search_steps(request):
    key_word = request.GET.get('key_word')
    type = request.GET.get('type')
    response_data = Step.searchStep(key_word, type)
    return HttpResponse(json.dumps(response_data, cls=DataEncoder), content_type="application/json")


def features(request):
    return render(request, 'auto/feature_list.html')

def viewDetail(request, feature_id):
    return render(request, 'auto/feature.html', {'featureId':feature_id})

def get_feature(request, feature_id):
    feature = Feature.objects.get(pk=feature_id)
    feature_dto = get_feature_dto(feature)
    return HttpResponse(json.dumps((feature_dto), cls=DataEncoder), content_type="application/json")


def get_feature_dto(feature):
    workspace = WorkSpace.objects.get(pk=feature.workspace)
    workspace_path = workspace.getFolderPath()
    dict = Step.getStepByFolder(workspace_path)
    file_path = FeatureFileGenerator.get_workspace_entrance(workspace)
    feature = lettuce.Feature.from_file(file_path)
    feature_dto = FeatureDto(feature.name, feature.description)
    scenarios = []
    for sce in feature.scenarios:
        s_dto = ScenarioDto('id_missing', sce.name)
        for s_item in sce.steps:
            co_func, patten, result = match_definision(s_item, dict)
            action_type, varlist_tuple, variables = extract_func_info(co_func, s_item, result)
            step_dto = StepDto()
            func_code = co_func.func_code
            step_dto.fill(func_code.co_filename, func_code.co_firstlineno, func_code.co_argcount,
                          varlist_tuple, func_code.co_name, co_func.func_name, action_type, variables, patten,
                          'id_no_use')
            s_dto.steps.append(step_dto)
        scenarios.append(s_dto)
    feature_dto.fill_scenarios(scenarios)
    return feature_dto


def list_features(request):
    features = Feature.objects.all()
    feature_dtos = []
    for feature in features:
        feature_dto = get_feature_dto(feature)
        feature_dto.set_id(feature.id)
        feature_dtos.append(feature_dto)
    return HttpResponse(json.dumps((feature_dtos),cls=DataEncoder), content_type="application/json")



@csrf_exempt
def save_feature(request):
    if request.method != 'POST':
        return HttpResponse("only post allowed")
    # elif: feature locked should early return
    else:
        json_data = request.body
        saver = StepDtoPostSaver()
        result = saver.save(json_data)
        workspace = WorkSpaceGenerater.gen_workspace('web')
        FeatureFileGenerator.save_feature_file(result, workspace, json_data)
        result.update_workspace(workspace)
        return HttpResponse(request.body)

@csrf_exempt
def update_feature(request, feature_id):
    if request.method != 'POST':
        return HttpResponse("only post allowed")
    # elif: feature locked should early return
    else:
        json_data = request.body
        updater = StepDtoPostUpdater()
        result = updater.update(json_data)
        workspace = WorkSpace.objects.get(pk=result.workspace)
        FeatureFileGenerator.update_feature_file(result, workspace)
        return HttpResponse(request.body)

def exe_feature(request, feature_id):
    result = ExecutionPlanSaver.save_execution_plan(feature_id)
    return HttpResponse("result:{0}".format(result))

def exe_feature_status(request, feature_id):
    result = Feature.objects.get(pk=feature_id)
    return HttpResponse("locked:{0}".format(result.executionLock))

def testplan(request, testplan_id):
    return render(request, 'auto/test_plan.html')

def list_testplans(request):
    return render(request, 'auto/test_plan_list.html')
