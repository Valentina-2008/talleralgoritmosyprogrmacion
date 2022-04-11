#Entradas 
valor_prenda=float(input("Ingrese valor de la prenda"))
#Caja negra
Descuento=valor_prenda*0.15
valor_total=valor_prenda-Descuento
#Salidas
print("Usted debe pagar:", valor_total)