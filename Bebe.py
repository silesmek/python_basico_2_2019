#1. Crear una clase 'Bebe'
#2. Declarar 4 acciones: respirar, comer, llorar, dormir
class Bebe:
    def respirar(self):
        print('El bebé respira')

    def comer(self):
        print('El bebé come')

    def llorar(self):
        print('Guaaaaaaaaaaaaaaaaaa!')

    def dormir(self):
        print('ZZZZZZZZZZZZZZZZZzzzzzzzzzzzzzzzzzzzz!')

#Nace un pato que se llama donald
dia_bebe=Bebe()
#Donald dice quack y camina
dia_bebe.respirar()
dia_bebe.llorar()
dia_bebe.comer()
dia_bebe.dormir()

#3. Simular un día normal de un bebé
print("Amanece y sale el sol.  El bebé despierta. \nComo tiene hambre, comienza a llorar... ")
dia_bebe.llorar()
print("La mamá carga al bebé y le da el biberón.")
dia_bebe.comer()
print("En la noche el bebé está cansado y tiene sueño. \nLa mamá lo acuesta en el cuna:")
dia_bebe.dormir()


