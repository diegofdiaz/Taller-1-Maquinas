from sympy.solvers import solve
from sympy import Symbol

x = Symbol('x')
w=solve((8*x+3)/(1+x))
print(w)