import sys
sys.path.append('../')
sys.path.append('../../')
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Feature, Scenario, Step
from dto import DateEncoder, StepDto
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
    return HttpResponse(json.dumps(response_data,cls=DateEncoder), content_type="application/json")

def sample(request):
    return render(request, 'auto/sample.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
