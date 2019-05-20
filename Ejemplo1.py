a=[1,3,5,8,7,9,2]
f=lambda x:x*10 #multiplica todo por 10

#otra forma
print([i*10 for i in a])
print([f(i) for i in a]) #iterar por cada elemento
print([(lambda x:x*10)(i) for i in a])
print([(lambda x:x*10)(i) for i in a if i>5]) #aplica la función a todo lo que sea mayor a 5 en a
