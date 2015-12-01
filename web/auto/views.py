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
import exceptions
import json
import pdb
from django.contrib.auth.decorators import login_required

def index(request):
    steps = Step.getStepByFolder('../simple-selenium')
    return render(request, 'auto/index.html', {'steps': steps})

@login_required()
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
    feature = Feature.objects.filter(id=feature_id).first()

    feature_dto = FeatureDto(feature.name, feature.description)
    scenarios = []
    for sce in feature.scenario_set.all().filter(deleted=0):
        s_dto = ScenarioDto(sce.id, sce.description)
        s_dto.fill_steps(sce)
        scenarios.append(s_dto)

    feature_dto.fill_scenarios(scenarios)
    return HttpResponse(json.dumps((feature_dto), cls=DataEncoder), content_type="application/json")


def list_features(request):
    features = Feature.objects.all()
    feature_dtos = []
    for feature in features:
        # pdb.set_trace()
        feature_dto = FeatureDto(feature.name, feature.description)
        feature_dto.set_id(feature.id)
        scenarios = []
        for sce in feature.scenario_set.all().filter(deleted=0):
            s_dto = ScenarioDto(sce.id, sce.description)
            scenarios.append(s_dto)            

        feature_dto.fill_scenarios(scenarios)
        feature_dtos.append(feature_dto)

    return HttpResponse(json.dumps((feature_dtos),cls=DataEncoder), content_type="application/json")



@csrf_exempt
def save_feature(request):
    if request.method != 'POST':
        return HttpResponse("only post allowed")
    # elif: feature locked should early return
    else:
        try:
            json_data = request.body
            saver = StepDtoPostSaver()
            result = saver.save(json_data)
            item_id = result.id;
            workspace = WorkSpaceGenerater.gen_workspace('web')
            FeatureFileGenerator.save_feature_file(result, workspace)
            result.update_workspace(workspace)
            return HttpResponse(item_id);
        except exceptions:
            return HttpResponse(content='error', content_type=None, status=500, reason='save error')


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
