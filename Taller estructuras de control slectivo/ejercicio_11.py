
#Entradas
t=float(input("Digite la temperatura:"))
#Caja negra
d=""
if(t>85 and t<=120):
    d="Natacion"
elif(t>70 and t<=85):
    d="Tennis"
elif(t>33 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esqui"
elif(t>=0 and t<=10):
    d="Marcha"
else:
    d="La temperatura no pertenece a ningun deporte"
#Salida
print(f"El deporte a practicar es: {d}")
