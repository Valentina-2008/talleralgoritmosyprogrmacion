#Entradas
departamento1=float(input("Ingrese el valor de las ventas del primer departamento"))
departamento2=float(input("Ingrese el valor de las ventas del segundo departamento"))
departamento3=float(input("Ingrese el valor de las ventas del tercer departamento"))
sueldo=float(input("Ingrese el valor del sueldo:"))
#Caja negra
sueldo1=""
sueldo2=""
sueldo3=""
ventast=departamento1+departamento2+departamento3   
porcentaje1=(ventast*33)/100
if(departamento1>porcentaje1):
    sueldo1=(sueldo*20)/100
elif(departamento2>porcentaje1):
    sueldo2=(sueldo*20)/100
elif(departamento3>porcentaje1):
    sueldo3=(sueldo*20)/100
else:
    sueldo1=sueldo
    sueldo2=sueldo
    sueldo3=sueldo
#Salida
print(f"El sueldo del departameno 1 es {sueldo1} el sueldo del departamento 2 es {sueldo2} y el sueldo del departamento 3 es {sueldo3}")

