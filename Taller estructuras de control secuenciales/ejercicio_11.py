#Entradas
nombre=str(input("Ingrese nombre del trabajador:"))
numero_horas=int(input("Ingrese el numero de horas trabajadas:"))
pago_hora=float(input("Ingrese el valor por hora:"))
horas_extra=int(input("Ingrese el numero de horas extras trabajadas"))
numero_hijos=int(input("Ingrese el numero de hijos:"))
sueldo_base=float(input("Ingrese sueldo base del trabajador:"))
#CAJA NEGRA
pago_horas_extra=(horas_extra*pago_hora+0.25)
deduccion1=sueldo_base-0.05
deduccion2=sueldo_base-0.02
deduccion3=sueldo_base-0.07
deduccion_total=deduccion1+deduccion2+deduccion3
pago_por_hijo=numero_hijos*173.000
sueldo_neto=sueldo_base+pago_horas_extra+pago_por_hijo+250.000+180.000
asignaciones=pago_por_hijo+250.000+180.000
#Salidas
print("El trabajador", nombre)
print("Tiene un salario neto de:", sueldo_neto)
print("El total de las asignaciones es de:", deduccion_total)
print("Sus asiganaciones son de:", asignaciones)



