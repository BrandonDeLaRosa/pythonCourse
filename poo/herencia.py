
class Vehicle:
    def __init__(self,make,color,model) -> None:
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):    
        print("Manufacturer", self.make)
        print("Color", self.color)
        print("Model", self.model)


class Car(Vehicle):    #? De Esye modo heredamos la info de vehicls en Car
    def __init__(self,make,color,model,doors) -> None:
        Vehicle.__init__(self,make,color,model)
        self.doors = doors #todo <--- elemento agregado al padre, desde la clase(hijo)

    def print_car_details(self):
        # Esta funcion concatena todo lo que hay en el metodo: print_details en Vehicle
        self.print_details()    #! Usando el metodo del padre en el hijo.
        print("Doors: ", self.doors)  #? para que al usar el metodo (print_car_details), se muestra tambien el numero de puertas.


coche = Car("Susuki", "Grey", 2015, 4)            
coche.print_car_details()  #todo Metodo hijo
print("Division entre funcion padre/hijo")
coche.print_details()      #todo metodo padre.

