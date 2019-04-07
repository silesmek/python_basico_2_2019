#Crear un código que calcule las soluciones de la ecuación cuadrática de la forma ax2+bx+c=0
import math
a=float(input("Por favor ingresar \"a\""))
b=float(input("Por favor ingresar \"b\""))
c=float(input("Por favor ingresar \"c\""))
discriminante=b ** 2 - 4 * a * c

#área=largo*ancho
if discriminante<0:
    raiz=math.sqrt(-discriminante)*complex(0.1)
else:
    raíz=math.sqrt(discriminante)
#x1=(-b+math.sqrt((b**2-4*a*c)))/(2*a)
#x2=(-b-math.sqrt((b**2-4*a*c)))/(2*a)
x1=(-b+raiz)/(2*a)
x2=(-b-raiz)/(2*a)
print("El valor de x1 es",x1)
print("El valor de x2 es",x2)
print(x1,x2)