#WHILE

import math

num=int(input("Digite un numero: "))

while num < 0:
    print("Ha ocurrido un error, ingrese un numero positivo")
    num = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es : {(math.sqrt(num)):.2f}")

i=0
while i <10:
    print("Hola Mundo")
    i+=1