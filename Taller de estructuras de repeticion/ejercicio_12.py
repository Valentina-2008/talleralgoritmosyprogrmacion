f=g=0
Nombre=""
porcentaje=""
f=""
g=""
while True:
    n=input("Nombre del estudiante:")
    p=float(input("Ingrese puntaje de estudiante:"))
    Nombre.append(n)
    porcentaje.append(p)
    c=float(input("Quiere continuar? /ndigite 0 para si y 1 para no"))
    if(c==1):
        break
for k in range((len(porcentaje))):
    if(porcentaje(k)<(sum(porcentaje)/len(porcentaje))):
        f+=1
        elif(porcentajE(k)<(sum(porcentaje)/len(porcentaje))):
            g+=1
f=round((f*100)/len(porcentaje),2)
g=round((f*100)/len(porcentaje),2)
a=b=0
r=porcentaje(0)
for i in range(len(porcentaje)):
    if(porcentaje(i)>r):
        r=porcentaje(i)
        a=i
print("El estudiante con mayor puntaje es:", Nombre(a))
for j in range(len(porcentaje)):
    if(porcentaje(j)<r):
        r=porcentaje(j)
        b=j
print("El estudiante con el menor puntaje es:", Nombre(j))
print("El promedio de los puntajes es:", round(sum(porcentaje/len(porcentaje),2)))











