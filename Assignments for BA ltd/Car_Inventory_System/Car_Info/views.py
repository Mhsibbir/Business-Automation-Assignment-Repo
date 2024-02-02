
from django.shortcuts import render
from .models import car_info_model
# Create your views here.
def car_info_form(request):
    
    return render(request,"formWValidation.html")

def save_info(request):
    if request.method =='POST':
        car_type = request.POST.get('carType')
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        battery_capacity = request.POST.get('batteryInput') 
        fuel_efficiency = request.POST.get('fuelInput')
        data = car_info_model(car_type=car_type,name=name,model=model,year=year,fuel_efficiency=fuel_efficiency,battery_capacity=battery_capacity)
        data.save()
        messege = 'Car information saved'
    return render(request,"success_save.html",{'message':messege})