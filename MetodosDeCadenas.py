"""Cadena de caracteres
upper()=convierte en mayusculas todas las letras de un string
lower()= las pasa a minuscula
capitalize()=pone la primera letra en mayuscula
count()=cuenta cuantas veces aparece una letra o una cadena de caracteres
find()=representa la posicion en la cual aparece un caracter o grupo de caracteres(contando del final)
isdigit()= devuele un booleano, nos dice si es un valor numerico o no lo es
isalum()=comprueba si son alfanumericos
isalpha()= comprobuea si hay solo letras(no cuenta los espacios)
split()=separa por palabras utilizando espacios
strip()=borra los espacios sobrantes al principio o al final
replace()=cambia una letra o palabra por otra en un string
rfind()=representa el indice de un caracter (contando desde el principio)
"""
nombreUsuario=input("Introduce tu nombre de Usuario: ")

print(f"El nombre es: {nombreUsuario.upper()} ")
print(f"El nombre es: {nombreUsuario.lower()} ")
print(f"El nombre es: {nombreUsuario.capitalize()} ")

edad=input("introduce la edad: ")

#print(edad.isdigit()) #dice si es un numero o no

while(edad.isdigit()==False): #Si no introduce un numero entra al while
    print("Por favor, introduce un valor numerico")
    edad=input("Introduce la edad: ")

if (int(edad)<18): #ponemos el int porque la edad la guardamos con un input y el input se guarda solo lo que son cadenas de caracteres, entonces
    print("No puede pasar")             #con el int le decimos que lo haga numerico
else:
    print("puedes pasar")
