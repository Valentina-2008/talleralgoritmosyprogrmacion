#Entradas
capital=float(input("Ingrese cantidad de prestamo:"))
pago=float(input("Ingrese cantidad pagada:"))
tiempo=int(input("Ingrese el tiempo:"))
#Caja negra
intereses=(pago-capital)/capital
r=(intereses*100)/(capital*tiempo)
porcentaje=(capital*tiempo*r)/100
#Salidas
print("El porcentaje de interes es de:", porcentaje)