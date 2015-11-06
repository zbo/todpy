import sys
sys.path.append('../')
sys.path.append('../../')
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Feature, Scenario, Step
from dto import DataEncoder, StepDto, FeatureDto, ScenarioDto
from django.views.decorators.csrf import csrf_exempt
from auto.saver import StepDtoPostSaver
import json
import pdb

def index(request):
    steps=Step.getStepByFolder('../simple-selenium')
    return render(request, 'auto/index.html', {'steps': steps})

def create(request):
    return render(request, 'auto/create.html')

# http://localhost:8000/auto/search_steps?key_word=aaa&type=ios
def search_steps(request):
    key_word = request.GET.get('key_word')
    type=request.GET.get('type')
    response_data=Step.searchStep(key_word,type)
    return HttpResponse(json.dumps(response_data,cls=DataEncoder), content_type="application/json")

@csrf_exempt
def save_feature(request):
    if request.method != 'POST':
        return HttpResponse("only post allowed")
    else:
        json_data=request.body
        saver = StepDtoPostSaver()
        result = saver.save(json_data)
        return HttpResponse(request.body)

def get_feature(request, feature_id):
    feature = Feature.objects.filter(id=feature_id).first()
    feature_dto = FeatureDto(feature.name, feature.description)
    scenarios = []
    for sce in feature.scenario_set.all():
        s_dto = ScenarioDto(sce.description)
        s_dto.fill_steps(sce.step_set.all())

        scenarios.append(s_dto)
    feature_dto.fill_scenarios(scenarios)
    return HttpResponse(json.dumps((feature_dto),cls=DataEncoder), content_type="application/json")

