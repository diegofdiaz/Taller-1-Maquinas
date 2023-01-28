import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as c
from scipy.optimize import fsolve

def Magn(H):
    return ((2*10*-3)*H)/(1+((10*-3) *H))-B_enth#Curva de magnetizacion 

#datos 
i=0.5 #Amperes
N= 1000 #Espiras
L_nucleo= 1#metro
L_enth=0.001 #metros
S= 20 #cm^2
H=np.arange(0,10000,0.1)
Magn=lambda H: ((2*10*-3)*H)/(1+((10*-3) *H))-B_enth#Curva de magnetizacion 

F_tot=N*i #Criterio de parada
B_enth= 1# float(input("ingrese una primera estimacion para B"))#Tesla

paso=0.1
F_calc=0
error =100 # inicializando variable 

while error > np.abs(3):
    H_enth=B_enth/c.mu_0
    U_enth=H_enth*L_enth 

    H_hierro=fsolve(Magn,[1,1])[0]
    U_hierro=H_hierro*L_nucleo

    F_calc= U_hierro+U_enth
    error=((F_tot-F_calc)/F_tot)*100
    print ("se calcula "+str(F_calc)+"con un error de" + str(error))
    print ("el valor de B es " +str (B_enth))

    # cambio de valor a probar 
    if error >0:
        B_enth-=paso
    else:
        B_enth+=paso
    print(error)