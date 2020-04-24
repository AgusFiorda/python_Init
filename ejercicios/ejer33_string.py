

"""• Crea un programa que pida introducir una dirección de email por teclado. El programa debe imprimir en consola si
la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección
será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la
dirección de email o al final, la dirección también será errónea,"""


direccion=input("Escriba una direccion de email: ")

arroba = direccion.count("@") #cuenta las @ que aparecen
posini = direccion.rfind("@") #cuenta si esta en la posicion inicial
cort = direccion[(len(direccion)-1):len(direccion)] #para fijarse la ultima posicion

while(arroba>1 or posini==0 or cort=="@"):
    print("El correo que introdujo es invalido.Escriba su correo nuevamente.")
    direccion = input("Escriba una direccion de email: ")

print("Correo valido,¡Muchas gracias!")
