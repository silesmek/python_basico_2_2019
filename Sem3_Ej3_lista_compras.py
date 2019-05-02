#lista de compras
lista_de_compras=[]
verduras=['tomates','papas','cebollas','ajos']
frutas=['piña','naranja','sandía']
carnes=['mortadela','pollo','costilla de cerdo']
limpieza=['jabon','cloro','shampoo']
lista_de_compras=[verduras,frutas,carnes,limpieza]
#lista_de_compras.append([verduras,frutas,carnes,limpieza])
pass
"""cantidad=0
for categoria in lista_de_compras:
    cantidad += len(categoria)
print(cantidad)
"""
"""mi_lista=[]
for categoria in lista_de_compras:
    mi_lista.extend(categoria)
    print(mi_lista)
print(len(mi_lista))"""

mi_lista=[]
for categoria in lista_de_compras:
    mi_lista.extend(categoria)
print(len(mi_lista))