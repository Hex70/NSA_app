from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Device(models.Model):
    id: models.IntegerField()
    IP_address = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200,default='', blank=True)
    username = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    device_location = models.CharField(max_length=200,default='', blank=True)
    vendor = models.CharField(max_length=200,default='', blank=True)
    device_model = models.CharField(max_length=200,default='', blank=True)
    ios_version = models.CharField(max_length=200,default='', blank=True)


class Device_State (models.Model):
    id: models.IntegerField()
    device = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Last_scan = models.CharField(max_length=200,default='/')
    State  = models.CharField(max_length=200,default='/')
    last_backup = models.CharField(max_length=200,default='/')
    backup_time = models.CharField(max_length=200,default='/')
   

class Details (models.Model):
    id: models.IntegerField()
    device = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name  = models.CharField(max_length=200,default='/')
    time   = models.CharField(max_length=200,default='/')
    detected_vuln = models.CharField(max_length=200,default='/')
    fixed_vuln = models.CharField(max_length=200,default='/')
    configuration_after_fix = models.CharField(max_length=200,default='/')
    configuration_before_fix = models.CharField(max_length=200,default='/')