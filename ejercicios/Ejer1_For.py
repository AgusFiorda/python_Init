"""Ejercicio 1:
• Crea un programa que muestre los números impares del 1 al 100.
Los números deberán aparecer una al lado del otro sin salto de línea."""
"""print("Ejercicio 1:")
impares=[]

for i in range(100):
    if i%2!=0:
        impares=i
        print({impares},end="")
"""
"""Ejercicio 2:
• Crea un programa que pida por teclado introducir una contraseña. 
La contraseña no podrá tener menos de 8 caracteres ni 
espacios en blanco. Si la contraseña es correcta, el programa imprime 
“Contraseña OK”. En caso contrario imprime “Contraseña errónea”
"""

"""print(" ")
print("\nEjercicio 2:")
contra=input("Introducir contraseña:")
cont=len(contra)

if cont>8 or contra=="":
    print("Contraseña OK")
else:print("Contraseña erronea")"""

"""Ejercicio 3"""
"""• Crea un programa que evalúe si una dirección de correo electrónico es válida 
o no en función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se 
considera correcta si solo tiene una “@” y si tiene uno o más “.”
"""
valido=False
puntos=False
email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
    if email[i]==".":
        puntos=True

cort=email[(len(email)-4):len(email)] #nos fijamos que el mail termine en .com


if valido==True and puntos==True and cort==".com":
    print("El email es correcto")

else:
    print("El email es incorrecto")


