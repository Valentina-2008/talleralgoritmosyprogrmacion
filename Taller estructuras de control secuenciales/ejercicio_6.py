#Entradas
Mujeres=int(input("Digite la cantidad de Mujeres: "))
Hombres=int(input("Digite la cantidad de Hombres: "))
#Caja negra
Total_estudiantes=Mujeres+Hombres#int
Mp=(Mujeres*100)/Total_estudiantes#float
Hp=(Hombres*100)/Total_estudiantes#float

#Salidas
print(f"El porcentaje de: {round(Mp,2)} y el porcentaje de Hombres: {round(Hp,2)}")