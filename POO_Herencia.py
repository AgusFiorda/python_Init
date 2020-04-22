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

class Moto(Vehiculos): #para heredar se escribe dentro de los parentesis la clase que va a heredar la nueva clase
    pass

miMoto=Moto("Honda","Tornado")
miMoto.estado()

