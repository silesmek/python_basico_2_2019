#Obtener el valor mayor sin usar ni max ni sort
lista=[10,2,7,1,9,2]
m=0
for i in range (0,len(lista)):
    if lista[i]>=m:
        m=lista[i]

print(m)