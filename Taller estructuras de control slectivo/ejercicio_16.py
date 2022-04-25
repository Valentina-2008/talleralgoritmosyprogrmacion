#entrada
nh=float(input("Ingrese el nivel de hemoglobina:"))
e1=str(input("Ingrese si la edad es mes o año:"))
e=int(input("Ingrese la edad del paciente :"))
s=str(input("ingrese el genero del paciente Mmujer/hombre:"))
#caja negra
r=""
if(e1=="mes" and 0<e<=1 and 13<nh<26):
    r="negativo"
elif(e1=="mes" and 1<e<=6 and 10<nh<18):
    r="negativo"
elif(e1=="mes" and 6<e<=12 and 11<nh<15):
    r="negativo"
elif(e1=="año" and 1<e<=5 and 11.5<nh<15):
    r="negativo"
elif(e1=="año" and 5<e<=10 and 12.6<nh<15.5):
    r="negativo"
elif(e1=="año"and 10<e<=15 and 14<nh<15.5):
    r="negativo"
elif(s=="mujer" and e1=="año" and e>15 and 12<nh<16):
    r="negativo"
elif(s=="hombre" and e1=="año" and e>15 and 14<nh<18):
    r="negativo"
else:
    r="positivo"

#salida
print(f"el paciente es {r} para anemia")