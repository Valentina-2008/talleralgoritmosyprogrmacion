#entradas
valor_pagado=float(input("Ingrese el valor pagado:"))
PVP=float(input("Ingrese el valor de venta al publico "))
#Caja negra
diferencia=PVP-valor_pagado
porcentaje=(diferencia/valor_pagado)*100
#Salida
print(f"El descuento es de: {porcentaje} %" )