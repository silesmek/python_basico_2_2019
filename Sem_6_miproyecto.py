#esto es un proyecto que usa otros módulos

from archivo1 import suma_resta #me lo pone en gris si aún no lo he usado

resultado=suma_resta(a=10,b=3,c=2)
print(resultado)

from archivo2 import mi_lista
from archivo2 import mi_diccionario
#from archivo2 import mi_lista,mi_diccionario

print('Esto es un ejemplo')
from subfolder.archivo3 import Pato
donald=Pato()
#print(donald.camina())
p=donald.camina()
mi_lista.append(7)
pass