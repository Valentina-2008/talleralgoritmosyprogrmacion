""""
sueldo-->float
salidas-->nuevo sueldo
"""
#Entradas
saldo_trabajador=float(input("Ingrese el saldo del trabajador:"))
#Caja negra
if(saldo_trabajador<900000):
    aumento=(saldo_trabajador*0.15)
elif(saldo_trabajador>900000):
    aumento=(saldo_trabajador*0.12)
print("El nuevo sueldo del trabajador es:", aumento)

