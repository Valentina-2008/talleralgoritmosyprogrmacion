c1=0
c2=0
c3=0
c4=0
promedioe=0
ce=0
total=0
while(c1>=0):
    co=str(input("consume licor? si/no:"))
    if(co=="si"):
        p=int(input("Que licor prefiere 1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro:"))
        c1=c1+1
        
            
    e=int(input("cual es su edad:"))
    ce=1+ce
    s=str(input("Ingrese su genero: hombre/mujer:"))
    if(s=="mujer" and e<18):
        c2=c2+1
    
    f=str(input("Desea seguir en la encuesta: si/no"))
    total=total+1
    if(s=="hombre" and 20<e<25 and p!=1):
            c3=c3+1
            if(p==5):
                c4=c4+1
            if(p==3):
                promedioe=(promedioe+e)/ce
            
    
    if(f=="no"):
        break
    else:
        continue

promediow=c4/total
#salida
print(f"Total, de personas encuestadas que consumen licor:{c1}")
print(f"Total, de mujeres menores de edad:{c2}")
print(f"Total, de hombres que no consumen aguardiente y que tienen entre 20 y 25 años de edad:{c3}")
print(f"Promedio de edad de las personas que consumen cerveza:{promedioe}")
print(f"Porcentaje de personas que consumen whisky en relación con el total encuestado:{promediow}")