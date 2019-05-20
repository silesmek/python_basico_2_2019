class Duck:
    def __init__(self,nombre):
        self.duck_nombre=nombre

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

#Nace un pato llamado donald
donald=Duck('donald')
#Donald dice quack y camina
donald.quack()
donald.walk()
print('Cuál es tu nombre?',donald.duck_nombre)