#Entradas
numero_de_horas=int(input("Ingrese numero de horas:"))
precio_hora=float(input("Ingrese valor hora:"))
sueldo_base=float(input("Ingrese sueldo base:"))
#Caja negra
descuento=sueldo_base*0.20
salario_neto=(numero_de_horas*precio_hora)-descuento
#Salidas
print("El sueldo neto es:", salario_neto)

