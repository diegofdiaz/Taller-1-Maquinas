#By diegofdiaz
#Codio utilizando para la generación de las graficas
import numpy as np
import matplotlib.pyplot as plt
#-------Declaración de variables utiles-----------
delta=0.01 #Representa el paso entre cada data a graficar
h=np.arange(0,50000+delta,delta)
b=(((1.8*10**(-3))*h)/(1+(10**(-3)*h)))
plt.plot(h,b)
plt.show()


#-------------Primer dato---------------
#flujo1=1*(10**(-3)) #Wb
#b1=