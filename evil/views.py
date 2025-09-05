from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import EvilEntity

def index(request): 
  return render(request, "evil/index.html")

def showcreature(request, evilentity_id):
  entity = get_object_or_404(EvilEntity, pk=evilentity_id)
  return render(request, "evil/showcreature.html", {"entity": entity})