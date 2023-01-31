import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
from scipy import constants as c
ur=200 # permitividad relatividad, variable de entrada
u=ur*c.mu_0
x = Symbol('x')
h1=solve((((2*10**(-3)))/(1+(10**(-3)*x))-u))
b1=u*h1[0]
he=b1/c.mu_0
Fr=0.5*1000
Fre=h1[0]*1 +he* 0.001
error_a= Fre-Fr
error_r= (abs(Fre-Fr)/Fr)*100
while error_r > 3:
    print(error_a)
    if error_a < 0:
        ur-=+10
    else:
        ur+=10
    u=ur*c.mu_0
    x = Symbol('x')
    h1=solve((((2*10**(-3)))/(1+(10**(-3)*x))-u))
    b1=u*h1[0]
    he=b1/c.mu_0
    Fr=0.5*1000
    Fre=h1[0]*1 +he* 0.001
    error_a= Fre-Fr
    error_r=(abs(Fre-Fr)/Fr)*100
print("El valor de la fuerza magnetomotriz encontrada fué :"+ str(Fre)+ ". Lo anterior con un error relativo de: ", error_r , "%")
print("El valor de B encontrado fué: ", b1)
