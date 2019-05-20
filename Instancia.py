#Creación de una instancia
#Ejemplo de objetos del tipo animal

class Animal:
    def __init__(self,e,a):
        self.especie=e
        self.edad=a
    def correr(self):
        print('Soy un {}.'
              'Estoy corriendo'.format(self.especie))

    def crecer(self,edad=0):
        if(self.edad+edad)>14:
            self.vivo=False

        else:
            self.edad+=edad
            self.vivo=True

#Se instancia un perro
perro=Animal('perro',3)

#Para obtener algunos atributos
print("hola soy un {} " 
      "tengo {} años".format(perro.especie,perro.edad))

#Se pueden ejecutar algunas funciones

perro.crecer(10)
print("hola soy un {} " 
      "tengo {} años".format(perro.especie,perro.edad))
#perro.crecer(-10)
perro.crecer(2)
#adicionalmente se pueden consultar atributos

if perro.vivo:
    print("hola soy un {} "
          "tengo {} años".format(perro.especie, perro.edad))
else:
    print('...Me morí...RIP')