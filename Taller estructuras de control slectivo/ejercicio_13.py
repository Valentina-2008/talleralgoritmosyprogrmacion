from datetime import datetime
#Saca fecha del sistema
ahora= datetime.now()
año_actual = ahora.year
mes_actual = ahora.month
dia_actual = ahora.day
#Año de nacimento con forma AÑO/MES/DIA
fecha_de_nacimiento=input("Digite fecha de nacimiento:")
año_de_nacimiento,mes_nacimiento,dia_nacimiento=fecha_de_nacimiento.split("/")
año_de_nacimiento=int(año_de_nacimiento)
mes_nacimiento=int(mes_nacimiento)
dia_nacimiento=int(dia_nacimiento)
#Calcular edad
zodiaco=""
if((mes_nacimiento>=11 and dia_nacimiento>=22)) and (mes_nacimiento<=12 and dia_nacimiento<=21):
    zodiaco="Sagitario"
elif((mes_nacimiento>=12 and dia_nacimiento>=22)) and (mes_nacimiento<=1 and dia_nacimiento<=20):
    zodiaco="Capricornio"
elif(mes_nacimiento>=1 and dia_nacimiento>=1) and (mes_nacimiento<=2 and dia_nacimiento<=19):
    zodiaco="Acuario"
elif(mes_nacimiento>=2 and dia_nacimiento>=20) and (mes_nacimiento<=3 and dia_nacimiento<=19):
    zodiaco="Piscis"
elif(mes_nacimiento>=3 and dia_nacimiento>=21) and (mes_nacimiento<=4 and dia_nacimiento<=20):
    zodiaco="Aries"
elif(mes_nacimiento>=4 and dia_nacimiento>=21) and (mes_nacimiento<=5 and dia_nacimiento<=21):
    zodiaco="Tauro"
elif(mes_nacimiento>=5 and dia_nacimiento>=22) and (mes_nacimiento<=6 and dia_nacimiento<=21):
    zoadiaco="Geminis"
elif(mes_nacimiento>=6 and dia_nacimiento>=22) and (mes_nacimiento<=7 and dia_nacimiento<=22):
    zoadiaco="Cancer"
elif(mes_nacimiento>=7 and dia_nacimiento>=23) and (mes_nacimiento<=8 and dia_nacimiento<=23):
    zodiaco="Leo"
elif(mes_nacimiento>=8 and dia_nacimiento>=24) and (mes_nacimiento<=9 and dia_nacimiento<=22):
    zodiaco="Virgo"
elif(mes_nacimiento>=9 and dia_nacimiento>=23) and (mes_nacimiento<=10 and dia_nacimiento<=22):
    zodiaco="Libra"
elif(mes_nacimiento>=10 and dia_nacimiento>=23) and (mes_nacimiento<=11 and dia_nacimiento<=21):
    zodiaco="Escorpio"
#Salidas
print(f"su signo es: {zodiaco}")
