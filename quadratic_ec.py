from math import sqrt

'''
Este programa calcula los valores de x1 y x2 de una ecuación cuadrática,
cuyos valores de a, b y c son dados por el usuario.
'''

# 1. Mostrar al usuario la forma general de la ecuación cuadrática
print('Forma general de la ecuación cuadrática: ax^2 + bx + c = 0')

# 2. Solicitar al usuario los valores de a, b y c, y convertirlos en números decimales
a = float(input('Inserte el valor de a: '))
b = float(input('Inserte el valor de b: '))
c = float(input('Inserte el valor de c: '))

print('La forma de la cuadrática dada es: ', a, 'x^2 + ', b, 'x + ', c, " = 0" )

# 3. Calcular el valor de x1 y x2, y detener el programa si se obtienen raices imaginarias
if b**2 < 4*a*c:
    print('Error, su ecuación cuadrática contiene una o más raíces imaginarias')
else:     
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print("Las raíces de la ecuación son:")
    print("x1 = ", x1)
    print("x2 = ", x2)
