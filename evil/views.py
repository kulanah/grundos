from django.shortcuts import get_object_or_404, render
import json

from .models import EvilEntity

def index(request): 
  return render(request, "evil/index.html")

def showcreature(request, evilentity_id):
  json_data = open('evil/static/entities.json')
  entity_list = json.load(json_data)["entities"]
  entity = entity_list[evilentity_id - 1]
  prev_index = evilentity_id - 1 if evilentity_id > 1 else len(entity_list)
  next_index = evilentity_id + 1 if evilentity_id < len(entity_list) else 1
  return render(
    request, 
    "evil/showcreature.html", 
    {
      "entity_name": entity["name"], 
      "entity_entry": entity["description"],
      "entity_image": entity["image_source"],
      "entity_alt_text": entity["image_alt_text"],
      "selected_id": evilentity_id,
      "entity_list": entity_list,
      "prev_index": prev_index,
      "next_index": next_index
    }
  )