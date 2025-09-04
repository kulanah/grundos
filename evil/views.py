from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
  return HttpResponse("Hello world")

def detail(request, evilentity_id):
  return HttpResponse("You're looking at entity %s." % evilentity_id)