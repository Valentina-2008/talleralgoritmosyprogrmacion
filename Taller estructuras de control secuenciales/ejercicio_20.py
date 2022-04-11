P=float(input("Ingrese valor del computador:"))
t=float(input("Ingrese valor de cada cuota:"))
#Caja negra
total_de_cuota=t*12
diferencia=total_de_cuota*12
dif=total_de_cuota-P
porcentaje=(dif/P)*100
#Salidas
print("El porcentaje de aumento es:", porcentaje)
