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
x = Symbol('x')
#-------------Primer dato---------------
flujo1=1*(10**(-3)) #Wb
b1=(flujo1/(0.004))
h1=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b1))
print(h1)
#plt.plot(h1,b1, marker="o", color="red")
#plt.show()
#-------------segundo dato---------------
flujo2=5*(10**(-3)) #Wb
b2=(flujo2/(0.004))
h2=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b2))
print(h2)
#-------------tercer dato---------------
flujo3=7*(10**(-3)) #Wb
b3=(flujo3/(0.004))
h3=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b3))
print(h3)
#-------------------Graficas-------------------
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
ax1.plot(h,b)
ax1.plot(h1,b1, marker="o", color="red")
ax2.plot(h,b)
ax2.plot(h2,b2, marker="o", color="red")
ax3.plot(h,b)
ax3.plot(h3,b3, marker="o", color="red")
ax4.plot(h,b)
plt.show()

