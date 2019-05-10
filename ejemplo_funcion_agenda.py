agenda={
    'Juan Pérez':{'teléfono':'83013040',
                  'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'teléfono':'87001030',
                    'correo':'crojas@hotmail.com'},
    'Ana Marín':{'teléfono':'910013',
                 'correo':'Ana@marin.com'}
}
"""
def fun_agenda():
    nombre=input("Nombre:")
    telefono=input("Teléfono:")
    correo=input("Correo:")
    agenda[nombre] = {telefono,correo}
fun_agenda()
print(agenda)
"""
def agregar_contact(nombre,telefono,correo):
    #agenda.update({nomobre:
     #                  {'telefono':telefono,
     #                   'correo':correo}})

    agenda[nombre]={'telefono':telefono,
                'correo':correo}

agregar_contact(nombre='felipe',
                telefono=54548,
                correo='felipe@hotmail.com')
print(agenda)