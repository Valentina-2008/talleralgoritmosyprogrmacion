l=float(input("Ingrese el valor de la lectura anterior:"))
a=float(input("Ingrese el valor de la lectura actual:"))
#caja negra
d=a-l
v=""
if(0<d<100):
    v=4600
elif(101<d<300):
    v=8000
elif(301<d<500):
    v=100000
elif(d>501):
    v=120000
m=d*v
#salida
print(f"El valor a pagar por suscriptor por concepto de consumo de luz eléctrica y servicio de aseo urbano es : {m}")