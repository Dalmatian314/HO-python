import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



tabla= np.loadtxt("archivo.dat")
x =tabla[:,0]
y =tabla[:,1]
#plt.plot(x,y) 
#plt.show()

p = np.poly1d(np.polyfit(x, y, 1))

t = np.linspace(3, 10, 400)
plt.plot(x, y, 'o', t, p(t), '-')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

