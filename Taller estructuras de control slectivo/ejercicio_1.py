""""
Entradas
intereses-->float
inversion-->float
Salidas
dinero final-->float
"""
#Entradas
intereses=float(input("Ingrese el valor de los intereses:"))
inversion=float(input("Ingrese el valor de inversion:"))
#Caja negra
if(intereses>100.000):
    cuenta=intereses*inversion
else:
    cuenta="No reinvertira el dinero"
#Salida
print("El dinero final en la cuenta es:", cuenta)
