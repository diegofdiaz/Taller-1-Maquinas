import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
flujo1=1*(10**(-3)) #Wb
b1=(flujo1/(0.004))
h1=solve((((1.8*10**(-3))*x)/(1+(10**(-3)*x))-b1))
print(h1)