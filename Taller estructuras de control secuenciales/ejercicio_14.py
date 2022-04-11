#Entradas
lectura1=float(input("Ingrese monto de la lectura anterior:"))
lectura2=float(input("Ingrese monto de la lectura actual"))
costo_Kilovatios=float(input("Ingrese costo por kilovatio:"))
#Caja negra
lectura=lectura2-lectura1
total_costo=lectura*costo_Kilovatios
#Salidas
print("El costo total a pagar es:",total_costo)