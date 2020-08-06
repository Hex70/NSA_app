from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:device_id>/delete', views.deleteDevice, name="deleteDevice"),
    path('add', views.add_device, name='add_device'),
    path('adddevice', views.add_deviceclick, name='add_deviceclick'),
    path('<int:device_id>/analyse', views.Analyse, name="Analyse"),
    
    
## path('about', views.about, name='about'),

  ]