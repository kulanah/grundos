from django.shortcuts import get_object_or_404, render

from .models import EvilEntity

def index(request): 
  return render(request, "evil/index.html")

def showcreature(request, evilentity_id):
  entity = get_object_or_404(EvilEntity, pk=evilentity_id)
  entityList = EvilEntity.objects.order_by("id")
  return render(
    request, 
    "evil/showcreature.html", 
    {
      "entity": entity, 
      "entityList": entityList
    }
  )