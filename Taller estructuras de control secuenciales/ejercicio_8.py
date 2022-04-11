import math
#entrada
A=float(input("Ingrese lado a:"))
b=float(input("Ingrese lado b:"))
c=float(input("Ingrese lado c:"))
#caja negra
s=(A+b+c)/2
area=math.sqrt(s*(s-A)*(s-b)*(s-c))
#salida
print("el área es:",round(area,2))