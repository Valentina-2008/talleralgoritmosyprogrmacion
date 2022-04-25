#entardas
monto_compra=float(input("Ingrese el monto total de la compra:"))
intereses=float(input("Ingrese el valor de intereses:"))
#Caja negra
operacion=""
prestamo=""
restante=""
inte=""
if(monto_compra>5000000):
    operacion=(monto_compra*0.55)
elif(monto_compra>5000000):
    prestamo=(monto_compra*0.30)
elif(monto_compra>5000000):
    restante=(monto_compra*0.15)
elif(monto_compra<5000000):
    operacion=(monto_compra*0.70)
elif(monto_compra<5000000):
    restante=(monto_compra*0.30)
elif(monto_compra<5000000):
    inte=(intereses*0.20)
#Salidas
print(f"La empreesa invierte {operacion} , la cantidad a pagar de credito es {prestamo} , el total de credito es de {restante} y los interes a pagar son {inte}")


