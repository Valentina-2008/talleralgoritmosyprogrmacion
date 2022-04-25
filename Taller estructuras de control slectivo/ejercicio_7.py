#ENTRADA
km=float(input("Ingrese la cantidad de kilometros recorridos:"))
#CAJA NEGRA
pg=""
if(km<=300):
    pg="50.000"
elif(300<km<1000):
    pg=70000+(km-300)*30000
elif(km>1000):
    pg=150000+(km-1000)*9000
#salida
print(f"El valor a pagar es de: {pg}")