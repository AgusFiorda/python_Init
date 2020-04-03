#ejercicio 4
"""
Construir un programa que simule el funcionamiento de una calculadora
que puede realizar las 4 operaciones aritmeticas basicas(sumar,
restar,multiplicar y dividir).El usuario debe especificar la operacion
con el primer caracter del nombre de la operacion
"""

op= input(f"Elija la operacion que va a utilizar(s 'suma'/r 'resta'/d 'division'/m 'multiplicacion'): ").lower()

if op=="s":
    n1=int(input("Escriba el primer numero: "))
    n2=int(input("Escriba el segundo numero: "))
    res=n1+n2
    print(f"El resultado es: [{res}]")

elif op=="r":
    n1=int(input("Escriba el primer numero: "))
    n2=int(input("Escriba el segundo numero: "))
    res=n1-n2
    print(f"El resultado es: [{res}]")
elif op == "d":
    n1 = int(input("Escriba el primer numero: "))
    n2 = int(input("Escriba el segundo numero: "))
    res = n1 / n2
    print(f"El resultado es: [{res}]")
elif op=="m":
    n1=int(input("Escriba el primer numero: "))
    n2=int(input("Escriba el segundo numero: "))
    res=n1*n2
    print(f"El resultado es: [{res}]")



