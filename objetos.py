"""
class First:
    pass

a=First()
print(type(a))
"""
class First:
    def __init__(self): # es un método especial que permite inicializar el control de los objetos
        print('Constructor ejecutado')

f=First()
