from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import EvilEntity

def index(request): 
  return HttpResponse("Hello world")

def showcreature(request, evilentity_id):
  template = loader.get_template("evil/showcreature.html")
  entity = get_object_or_404(EvilEntity, pk=evilentity_id)
  return render(request, "evil/showcreature.html", {"entity": entity})