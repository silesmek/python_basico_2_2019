"""
#1. Hacer una función que imprima
*
**
***
****
donde h es la altura y el ancho
"""
def asterisco(h):
    for i in range (1,h+1):
        print("*"*i)

asterisco(7)