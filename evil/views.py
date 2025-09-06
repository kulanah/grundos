from django.shortcuts import get_object_or_404, render

from .models import EvilEntity

def index(request): 
  return render(request, "evil/index.html")

def showcreature(request, evilentity_id):
  entity = get_object_or_404(EvilEntity, pk=evilentity_id)
  entity_list = EvilEntity.objects.order_by("id")
  prev_index = evilentity_id - 1 if evilentity_id > 1 else len(entity_list)
  next_index = evilentity_id + 1 if evilentity_id < len(entity_list) else 1
  return render(
    request, 
    "evil/showcreature.html", 
    {
      "entity": entity, 
      "entity_list": entity_list,
      "prev_index": prev_index,
      "next_index": next_index
    }
  )