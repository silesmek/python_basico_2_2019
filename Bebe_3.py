#5.Crecer(edad=1)
class Bebe:
    def __init__(self,nombre,edad):
        self.bebe_nombre=nombre
        self.bebe_edad =edad

    def crecer(self,edad=0):
        self.bebe_edad+=edad


bebe=Bebe('Rubén',1)
print('Bebé, cómo te llamas? me llamo :',bebe.bebe_nombre)
bebe.crecer(1)
print("hola me llamo {} " 
      "tengo {} años".format(bebe.bebe_nombre,bebe.bebe_edad))
bebe.crecer(1)
print("hola me llamo {} " 
      "tengo {} años".format(bebe.bebe_nombre,bebe.bebe_edad))
bebe.crecer(1)
print("hola me llamo {} " 
      "tengo {} años".format(bebe.bebe_nombre,bebe.bebe_edad))