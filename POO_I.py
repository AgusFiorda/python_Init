class Coche():
    def __init__(self): #es el constructor: se inicializa los objetos que pertenecen a esa clase
        self.__largoChasis=250
        self.__anchoChasis=150
        self.__ruedas=4 #es para encapsular y que no se puede modificar desde el exterior, pero si en los metodos
        self.__enmarcha=False

    def arrancar(self,arrancamos):#para crear metodos
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.__chequeoInterno()

        if(self.__enmarcha and chequeo):
            print("El chequeo salio 'OK'")
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo no se puede arrancar el coche"


        else:

            return "el coche esta parado"



    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")

    def __chequeoInterno(self): #__ para encapsular el metodo
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


miCoche=Coche() #instanciar una clase /creamos un objeto


print(miCoche.arrancar(True))

miCoche.estado()





print("-------------A continuacion creamos el 2do objeto-------------")




miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()