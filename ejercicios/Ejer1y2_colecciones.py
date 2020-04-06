"""Colecciones - Ejercicio 1:
Escriba un programa donde tenga una lista y que,
a continuación, elimine los elementos repetidos,
por último mostrar la lista."""

lista=[1,2,3,4,5,6,7,1,2,2,3,4,4,5,6]

conjunto= set(lista) #al pasarlo a conjunto nos elimina
#los elementos repetidos
lista=list(conjunto)#lo volvemos a poner en una lista
print(conjunto)

"""Colecciones - Ejercicio 2: 
Escriba un programa que tenga dos listas y que, 
a continuación, cree las siguientes listas 
(en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas."""

a=["agustin",1,2,3,"melody"]
b=["melody",2,4,3,"monica"]

conjuntoa=set(a)
conjuntob=set(b)

c= conjuntoa & conjuntob
lista=list(c)
print(f"-Elementos que aparecen en ambas listas {lista}")
c=conjuntoa- conjuntob
lista=list(c)
print(f"-Elementos que aparece en la primera lista pero no en la segunda {lista}")
c=conjuntob- conjuntoa
lista=list(c)
print(f"-Elementos que aparece en la primera lista pero no en la segunda {lista}")

