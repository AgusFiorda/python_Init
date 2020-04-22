def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas")
    #no se va a ejecutar nada despues del raise porque estamos creando
    #un error, osea que si hay mas codigo no se va a ejecutar
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuidate..."

print(evaluaEdad(15))

import math
def calcularRaiz(n1):
    if n1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(n1)
op1=(int(input("digite un numero: ")))
try:
    print(calcularRaiz(op1))
except ValueError as ErrorDeNumeroNegativo: #le damos un nombre al error
    print(ErrorDeNumeroNegativo)
print("programa terminado")