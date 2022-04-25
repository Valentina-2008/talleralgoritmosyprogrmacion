#Entrada
sb=float(input("Ingrese el salario bruto:"))
c=int(input("Ingrese la categoria:"))
#caja negra
a=""
if(c==1 and 4300000<sb<5000000):
    a=0.1
elif(c==2 and 3600000<sb<4300000):
    a=0.15
elif(c==3 and 2000000<sb<3600000):
    a=0.2
elif(c==4 and 900000<sb<2000000):
    a=0.4
elif(c==5 and sb<900000):
    a=0.6
sbv=sb*(1+a)
#salida
print(f"la categoria es : {c} y su nuevo salario bruto es: {sbv}COP")