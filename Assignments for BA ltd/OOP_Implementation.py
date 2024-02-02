#base class for all type of cars
class Car:
    def __init__(self,name, model, year ):
        self.name = name
        self.model = model
        self.year= year

#class definition for Electric type car
class ElectricCar(Car):
    def __init__(self,name, model, year, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(name, model, int(year))

        #function for displaying Electric type car info
    def car_info_electric_car():
        x = ElectricCar(input("Name:"),input("Model:"),input("Year:"), input("Enter battery capacity(kWh):"))
        print("\nCar information:\n"+ str(x.year) +" "+ x.name +" "+ x.model + "\nFuel Efficiency:",x.battery_capacity+ "kWh")

#class definition for Gas type car
class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        self.fuel_efficiency = fuel_efficiency
        super().__init__(name, model, int(year))

        #function for displaying gas type car info
    def car_info_gascar():
        x = GasCar(input("Name:"),input("Model:"),input("Year:"), input("Enter Fuel Efficiency(MPG):"))
        print("\nCar information:\n"+ str(x.year) +" "+ x.name +" "+ x.model + "\nFuel Efficiency:",x.fuel_efficiency+ "MPG")
        
#fucntion for selecting car type
def car_type_selection():
    car_type = input("Enter car type(Electric/Gas):")
    if car_type == "Electric":
        ElectricCar.car_info_electric_car()
    elif car_type == "Gas":
        GasCar.car_info_gascar()
    
    
# for invalid inputs and redirection to initial state
    else:
         return print("\nPlease Re-run the program and Enter Valid input for Car type as given(Electric/Gas)\n")
    
    
car_type_selection()

    
    


