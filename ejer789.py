#Graficar el siguiente polinomio, su derivada y puntos extremos:  f(x)=x³+x²-4x+4

#  7. Colocar titulo a los ejes y agregarle  una grilla en ambos. Definir el rango de la función entre -10 y 10.
#  8. Colocar titulo y colores distintos para la función y la derivada.
#  9. Guardar los resultados de evaluar la función en el rango del punto a cada 0.1 unidades en un archivo de texto.


from matplotlib import pyplot
from sympy import Symbol
import numpy as np

#x = Symbol('x')
#y = x**3 + x**2 - 4*x + 4
#dy = y.diff(x)


def f1(x):
    return x**3 + x**2 - 4*x + 4

def f2(x):
    return 3*x**2 + 2*x -4



x = range(-10, 10)
fig, ax = pyplot.subplots()
ax.plot(x, [f1(i) for i in x], label='funcion')
ax.plot(x, [f2(i) for i in x], '--r', label='derivada')
##ax.axis('equal')
leg = ax.legend();

pyplot.xlabel("x")
pyplot.ylabel("y")


pyplot.xlim(-10, 10)
pyplot.ylim(-5, 15)

pyplot.grid(True)

pyplot.savefig("output.png")

pyplot.show()


funcion = [f1(i) for i in x]
derivada = [f2(i) for i in x]    

np.savetxt('salida.dat',np.column_stack((funcion,derivada)))

