# Escriba el codigo necesario para que al ejecutar python ejercicio2.py
# se cree una grafica con una funcion sinusoidal entre 0 y 2pi.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,2*np.pi,1000)
y = np.sin(x)

plt.plot(x,y,c = "m")
plt.xlabel("Rad")
plt.ylabel("FuncSin")
plt.title("Seno(x)")
plt.savefig("hola.png")
