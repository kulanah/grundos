from django.db import models

class EvilEntity(models.Model):
  entity_name = models.CharField(max_length=30)
  text_entry = models.CharField(max_length=1000)
  image_alt_text = models.CharField(max_length=100)
  image = models.ImageField(upload_to="entity_image", default='media\default.png')
