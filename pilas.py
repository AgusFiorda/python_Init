#pilas

pila= [1,2,3]

#agregando elementos por el final
pila.append(4)
pila.append(5)
print(pila)
#sacando elementos de la pila por el final

pila.pop()
print(pila)
#aparte de sacarlo te retorna el valor que saca(muestra el valor
# que saco)
n=pila.pop()
print(f"sacamos el elemento: {n}")
print(pila)