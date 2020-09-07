from django.db import models

# Create your models here.
class LABTABLE(models.Model):
    laboratory = models.CharField(max_length=30)
    bench = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class LABEquipment(models.Model):
    bench = models.CharField(max_length=30)
    equipment = models.CharField(max_length=30)
    sn = models.CharField(max_length=30)
    pn = models.CharField(max_length=30)