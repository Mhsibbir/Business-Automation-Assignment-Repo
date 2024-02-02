from django.contrib import admin
from .models import car_info_model
# Register your models here.
class car_info_model_admin(admin.ModelAdmin):
    list_display=('car_type','name','model','year','fuel_efficiency','battery_capacity')

admin.site.register(car_info_model, car_info_model_admin)

