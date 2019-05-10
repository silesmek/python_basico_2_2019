#Crear una agenda de contactos utilizando diccionario
"""
agenda={
    'Juan Pérez':['83013040','jperez@gmail.com'],
    'Carlos Rojas':['87001030','crojas@hotmail.com'],
    'Ana Marín':['910013','Ana@marin.com'],
}

#pass

agenda={
    'Juan Pérez':{'teléfono':'83013040',
                  'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'teléfono':'87001030',
                    'correo':'crojas@hotmail.com'},
    'Ana Marín':{'teléfono':'910013',
                 'correo':'Ana@marin.com'}
}
"""

agenda={
    ('Juan', 'Pérez'):{'telefono':'83013040',
                  'correo':'jperez@gmail.com'},
    'Carlos Rojas':{'telefono':'87001030',
                    'correo':'crojas@hotmail.com'},
    'Ana Marín':{'telefono':'910013',
                 'correo':'Ana@marin.com'}
}

#2.Cuántas personas hay en la agegnda?
print(len(agenda))
#3. Cuáles son los nombres de los contactos
print(agenda.keys())
print(tuple(agenda.keys()))
#4 Utilizando #1, imprima las informaciones de cada contacto
"""
for persona in agenda.keys():
    print('nombre:',persona,
          'telefono:',agenda[persona]['telefono'],
          'correo:',agenda[persona]['correo'])
"""
print('con items')
for persona,info in agenda.items():
    print('nombre:', persona,
          'telefono:', info['telefono'],
          'correo:', info['correo'])

#5 Suponga que Juan Pérez cambió de teléfono.  Ahora tiene 63101111 y 233333
agenda[('Juan', 'Pérez')]['telefono']=['63101111','233333']
#6 Tenemos un nuevo contacto
#agregar a Sofia

#opción 1: crear un diccionario para Sofía
sofia={'telefono':33333333,
       'correo':'sofia@gmail.com'}
agenda['Sofia Castro']=sofia

#opción 2:
agenda.update({'sofia alfaro':sofia})
pass
