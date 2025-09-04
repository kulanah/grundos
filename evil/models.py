from django.db import models

class EvilEntity(models.Model):
  entity_name = models.CharField(max_length=30)
  text_entry = models.CharField(max_length=1000)
