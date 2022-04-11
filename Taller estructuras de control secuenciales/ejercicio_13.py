#Entradas
n1=int(input("Ingrese cantidad de billetes de 50.000:"))
n2=int(input("Ingrese cantidad de billetes de 20.000:"))
n3=int(input("Ingrese cantidad de billetes de 10.000:"))
n4=int(input("Ingrese cantidad de billetes de 5.000:"))
n5=int(input("Ingrese cantidad de billetes de 2.000:"))
n6=int(input("Ingrese cantidad de billetes de 1.000"))
n7=int(input("Ingrese cantidad de billetes de 500:"))
n8=int(input("Ingrese cantidad de billetes de 100:"))
#Caja negra
n1_1=n1*50.000
n2_2=n2*20.000
n3_3=n3*10.000
n4_4=n4*5.000
n5_5=n5*2.000
n6_6=n6*1.000
n7_7=n7*500
n8_8=n8*100
total=n1_1+n2_2+n3_3+n4_4+n5_5+n6_6+n7_7+n8_8
#Salida
print("El dinero total del banco es:", total)