#Entradas
presupuesto_ginecologia=float(input("Ingrese presupuesto de area de ginecologia:"))
presupuesto_traumatologia=float(input("Ingrese presupuesto de area de traumatologia"))
presupuesto_pediatria=float(input("Ingrese presupuesto de area de pediatria:"))
#Caja negra
ginecologia=presupuesto_ginecologia*0.40
traumatologia=presupuesto_traumatologia*0.30
pediatria=presupuesto_pediatria*0.30
#Salidas
print("El presupuesto para ginecologia es de:", ginecologia)
print("El presupuesto para traumatologia es de:", traumatologia)
print("El presupuesto para pediatria es de:", pediatria)
