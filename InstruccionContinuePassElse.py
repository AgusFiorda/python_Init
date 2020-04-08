"""CONTINUE"""

nombre="Pildoras informaticas"
contador=0
for i in nombre:
    if i==" ":
        continue #lo que hace el continue em este
        # caso es cuando encuentra un
        # espacio " " ignora las instrucciones y
        # sigue contando osea no cuenta el espacio en blanco sigue contando los caracteres
    contador+=1

print(contador)

"""PASS"""
class Miclase:
    pass #es como si no estuviese

email=input("email: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)