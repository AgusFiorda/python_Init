class Vehiculos():

    def __init__(self, marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha==True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        sel.frena=True

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\n"
              f"En marcha: {self.enmarcha}\nAcelerando: {self.acelera}"
              f"\nFrenando: {self.frena}")

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculos): #para heredar se escribe dentro de los parentesis la clase que va a heredar la nueva clase
    hwilly=""
    def willy(self):
        self.hwilly="Voy haciendo willy"

    def estado(self): #sobre escritura de metodos
        print(f"Marca: {self.marca} \n Modelo: {self.modelo}\n"
              f"En marcha: {self.enmarcha}\nAcelerando: {self.acelera}"
              f"\nFrenando: {self.frena}\n{self.hwilly}")


class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo) #Super() llama al metodo de la clase padre

        self.autonomia=100

    def cargaEnergia(self):
        self.cargando==True


print("---------------MOTO-----------------")
miMoto=Moto("Honda","Tornado")
miMoto.willy()
miMoto.estado()

print("---------------FURGONETA-----------------")
miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("---------------VehiculosELECTRICOS-----------------")
class BicicletaElectrica(VElectricos,Vehiculos): #Herencia multiple
    pass



miBici=BicicletaElectrica("Orbea","hjd5")


