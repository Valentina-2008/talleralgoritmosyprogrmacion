#Entrada
n=str(input("Ingrese nombre del cliente:"))
mc=float(input("Ingrese el monto de la compra:"))
#caja negra
d=""
if(mc<50000):
    d=0
elif(50000<mc<=100000):
    d=5
elif(100000<mc<=700000):
    d=11
elif(700000<mc<=1500000):
    d=18
elif(mc>1500000):
    d=25
mp=(mc-(mc*(d/100)))
#salida
print(f" Nombre del cliente: {n}")
print(f"El monto de la compra es: {mc}")
print(f"El monto a pagar es de: {mp}")
print(f"El descuento a sido de: {d}%")