#COLAS

"""Primero que entra primero que sale"""

cola=["Maria","agustin","tomas","roque"]

#agregando elementos al final de la lista
cola.append("ernesto")


#sacando elementos por el principio

n=cola.pop(0) #le indicamos con el cero que saque el primero
print(f"Atendiendo a {n}")
print(f"quedan las siguientes personas {cola}")