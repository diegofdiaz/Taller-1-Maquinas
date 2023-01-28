#By diegofdiaz
#Codio utilizando para la generación de las graficas
import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
#-------Declaración de variables utiles-----------
delta=0.01 #Representa el paso entre cada data a graficar
h=np.arange(0,50000+delta,delta)
b=(((1.8*10**(-3))*h)/(1+(10**(-3)*h)))
plt.plot(h,b)
x = Symbol('x')

#-------------Primer dato---------------
flujo1=1*(10**(-3)) #Wb
b1=(flujo1/(0.004))
h1=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b1))
print(h1)
plt.plot(h1,b1, marker="o", color="red")
plt.show()