from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Step
import pdb

def index(request):
    steps=Step.getStepByFolder()
    print steps
    return render(request, 'auto/index.html', {'steps': steps})

def create(request):
    return render(request, 'auto/create.html')

def sample(request):
    return render(request, 'auto/sample.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)