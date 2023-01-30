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
#-------------Primer dato----------------
flujo1=1*(10**(-3)) #Wb
b1=(flujo1/(0.004))
print("b1=", b1)
h1=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b1)) #Solve entrega la solucion como una lista, llamar h[0]
print("h1=", h1)
he1=b1/(4*np.pi*10**(-7))
print("he1=", he1)
i1=((h1[0]*0.7)+(h1[0]*0.25)+(he1*1*10**(-3)))/(800)
print("I1=", i1)
#-------------segundo dato---------------
flujo2=5*(10**(-3)) #Wb
b2=(flujo2/(0.004))
print("b2=", b2)
h2=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b2))#Solve entrega la solucion como una lista, llamar h[0]
print("h2=", h2)
he2=b2/(4*np.pi*10**(-7))
print("he2=", he2)
i2=((h2[0]*0.7)+(h2[0]*0.25)+(he2*1*10**(-3)))/(800)
print("I2=", i2)
#-------------tercer dato----------------
flujo3=6.5*(10**(-3)) #Wb
b3=(flujo3/(0.004))
print("b3=", b3)
h3=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b3)) #Solve entrega la solucion como una lista, llamar h[0]
print("h3=", h3)
he3=b3/(4*np.pi*10**(-7))
print("he3=", he3)
i3=((h3[0]*0.7)+(h3[0]*0.25)+(he3*1*10**(-3)))/(800)
print("I3=", i3)
#---------------Graficas-----------------
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
ax1.plot(h,b)
ax1.plot(h1,b1, marker="o", color="red")
ax2.plot(h,b)
ax2.plot(h2,b2, marker="o", color="red")
ax3.plot(h,b)
ax3.plot(h3,b3, marker="o", color="red")
ax4.plot(h,b)
plt.show()

