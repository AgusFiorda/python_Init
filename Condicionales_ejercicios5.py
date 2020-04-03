"""ejercicio 5
Hacer un diagrama que simule un cajero automatico con un saldo
inicial de $1000 y tendra el siguiente menu de opciones
1. ingresar dinero
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. salir
"""

saldo=1000

print(f"Usted tiene un saldo inicial de $1000")
opcion= int(input(f" 1. ingresar dinero \n 2. Retirar dinero de la cuenta \n 3. Mostrar dinero disponible \n 4. salir \nOpcion:"))

if opcion==1:
    ing=int(input("Monto a ingresar: "))
    saldo+=ing
    print(f"Su nuevo saldo es de: [{saldo}]")
elif opcion==2:
     retirar = int(input("Monto a retirar: "))
     if retirar > saldo:
         print("No tiene ese dinero para retirar")
     else:
         saldo -= retirar
         print(f"Su nuevo saldo es de: {saldo}")
elif opcion==3:
    print(f"El dinero en su cuenta es: [${saldo}]")
elif opcion==4:
    print("Gracias por utilizar el cajero automatico")
else:
    print("La opcion ingresa no es valida")

