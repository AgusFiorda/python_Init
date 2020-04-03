#CONJUNTOS
"""
En este vídeo hablaremos sobre los conjuntos, que son un tipo de
colección donde los elementos se agregan de forma desordenada y
no pueden haber valores duplicados.
"""

conjunto= set()

conjunto= {1,2,3,4,"hola"}

conjunto.add(5)#agrega a lo ultimo
conjunto.discard(3) #elimina el numero 3
print(conjunto)
conjunto.clear() #borra todo
print(conjunto)
conjunto= {1,2,3,4,"hola"}
print(3 in conjunto) #busca en el conjunto
