#suma
# 1. Crear una calculadora que sume, reste, multiplique, divida, eleve a una potencia y obtenga la raiz usando lambdas.
suma=lambda x,y:x+y
resta=lambda x,y:x-y
multiple=lambda x,y:x*y
divide=lambda x,y:x/y
import math
potencia=lambda x,y:math.pow(x,y)
raiz=lambda x,y:math.pow(x,1/y)

x=3
y=2
lista_funciones=[suma,resta,multiple,divide,potencia,raiz]
for mi_funcion in lista_funciones:
    print('resultado=',mi_funcion(x,y))

# 2. Crear un diccionario de funciones que sume, reste...
"""
diccionario_funciones={
    'suma':lambda x,y:x+y,
    'resta':lambda x,y:x-y,
    'multiple': lambda x, y: x*y,
    'divide': lambda x, y: x/y,
    'potencia': lambda x, y:math.pow(x,y),
    'raiz': lambda x, y: math.pow(x,1/y)
}
"""
calculadora={
    'suma':suma,
    'resta':resta,
    'multiple':multiple,
    'divide': divide,
    'potencia': potencia,
    'raiz': raiz
}

# usando dict
print('usando dict')
for f in calculadora.keys():
    print('resultado=',calculadora[f](x,y))
# otra forma de hacerlo
print('usando dict')
for f in calculadora.values():
    print('resultado=',f(x,y))