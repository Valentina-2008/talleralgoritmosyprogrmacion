#Entradas
sueldo_base=float(input("Ingrese el saldo base:"))
venta1=float(input("Ingrese valor de la venta 1:"))
venta2=float(input("Ingrese valor venta 2:"))
venta3=float(input("Ingrese valor venta 3:"))
#Caja negra
promedio_ventas=(venta1+venta2+venta3)/3
sueldo_total=(sueldo_base)+promedio_ventas*0.10
#Salidas
print("El total de sus comisiones del mes es:", promedio_ventas)
print("Su sueldo total de comisiones mas su sueldo base es:", sueldo_total)
