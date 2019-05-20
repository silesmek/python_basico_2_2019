#Crear una clase Bebé que tenga nombre
#4. 'Bebé, cómo te llamas?'me llamo :

class Bebe:
    def __init__(self,nombre):
        self.bebe_nombre=nombre


bebe=Bebe('Rubén')
print('Bebé, cómo te llamas? me llamo :',bebe.bebe_nombre)