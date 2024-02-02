from django.db import models

# Create your models here.
class car_info_model(models.Model):
    car_type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    fuel_efficiency = models.CharField(max_length=10,null=True, blank=True)
    battery_capacity = models.CharField(max_length=10,null=True, blank=True)


