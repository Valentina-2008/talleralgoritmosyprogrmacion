#Entradas
from math import exp
import math


a=int(input("Ingrese valor de a:"))
b=int(input("Ingrese valor de b:"))
c=int(input("Ingrese valor de c:"))
d=int(input("Ingrese valor de d:"))
#Caja negra
if("d=0"):
    resultado=(a-c)*(a-c)
elif(d>0):
    resultado=(a-b)*(a-b)*(a-b)/d
#Salida
print("El resultado es:", resultado)


