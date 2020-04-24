class Coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")

print("-----------------moto--------------")

miVehiculo=Moto()
miVehiculo.desplazamiento()
print("-----------------coche--------------")

miCoche=Coche()
miCoche.desplazamiento()
print("-----------------camion--------------")

miVehiculo3=Camion()
miVehiculo3.desplazamiento()


print("-----------------USANDO LA FUNCION PARA UTILIZAR CUALQUIER VEHICULO--------------")
def desplazamientoVehiculo(vehiculo): #creamos una funcion para llamar al vehiculo y que cada uno se desplase a su forma
    vehiculo.desplazamiento()

desplazamientoVehiculo(miCoche)