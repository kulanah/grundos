from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("showcreature/<int:evilentity_id>/", views.showcreature, name="showcreature")
 ]