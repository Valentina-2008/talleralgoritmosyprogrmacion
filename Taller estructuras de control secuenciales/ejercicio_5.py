#Entradas 
Calificacion1_p=float(input("Ingrese valor calificacion 1:"))
Calificacion2_p=float(input("Ingrese valor calificacion 2:"))
Calificacion3_p=float(input("Ingrese valor calificacion 3:"))
calificacion_e=float(input("Ingrese calificacion examen:"))
trabajo_final=float(input("Ingrese calificacion trabajo final:"))
#Caja negra
Promedio_p=(Calificacion1_p+Calificacion2_p+Calificacion3_p)/3
promedioparcial=Promedio_p*0.55
calificacion_examen=calificacion_e*0.30
calificacion_trabajo_final=trabajo_final*0.15
nota_final=(promedioparcial+calificacion_examen+calificacion_trabajo_final)
#Salidas
print("Su nota final es: ", nota_final)