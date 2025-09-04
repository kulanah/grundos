from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
 path("<int:evilentity_id>/", views.showcreature, name="showcreature")]