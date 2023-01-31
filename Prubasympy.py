import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
from scipy import constants as c
ur=200 # permitividad relatividad, variable de entrada
u=ur*c.mu_0
x = Symbol('x')
h1=solve((((2*10**(-3)))/(1+(10**(-3)*x))-u))
print("El valor de h", h1)
b1=u*h1[0]
he=b1/c.mu_0
Fr=0.5*1000
Fre=h1[0]*1 +he* 0.001
print("Fuerza magnetomotriz experimental ",Fre)
error_a= Fre-Fr
error_r= (abs(Fre-Fr)/Fr)*100