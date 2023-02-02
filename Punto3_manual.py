from sympy.solvers import solve
from sympy import Symbol
from scipy import constants as c
def metodo_iterativo(ur):
    error_r=1000
    while error_r > 3:
        u=ur*c.mu_0
        x = Symbol('x')
        h1=solve((((2*10**(-3)))/(1+(10**(-3)*x))-u))
        print("El valor de h", h1)
        b1=u*h1[0]
        print("El Valor de b es", b1)
        he=b1/c.mu_0
        print("El valor de he es:", he)
        Fr=0.5*1000
        Fre=h1[0]*1 +he* 0.001
        print("Fuerza magnetomotriz experimental ",Fre)
        error_a= Fre-Fr
        print("El error absoluto es: ", error_a)
        error_r= (abs(Fre-Fr)/Fr)*100
        print("El error relativo es:", error_r)
        ur= input("Digite un  nuevo valor de permitividad: ") # permitividad relatividad, variable de entrada 
ur= float(input("Digite un valor de permitividad inicial: "))# permitividad relatividad, variable de entrada
metodo_iterativo(ur)







# u=ur*c.mu_0
# x = Symbol('x')
# h1=solve((((2*10**(-3)))/(1+(10**(-3)*x))-u))
# print("El valor de h", h1)
# b1=u*h1[0]
# print("El Valor de b es", b1)
# he=b1/c.mu_0
# print("El valor de he es:", he)
# Fr=0.5*1000
# Fre=h1[0]*1 +he* 0.001
# print("Fuerza magnetomotriz experimental ",Fre)
# error_a= Fre-Fr
# print("El error absoluto es: ", error_a)
# error_r= (abs(Fre-Fr)/Fr)*100
# print("El error relativo es:", error_r)