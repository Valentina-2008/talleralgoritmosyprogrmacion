#Entradas
chelines_austriacos=float(input("Ingrese cantidad monetaria de chelines austriacos:"))
dracmas_griegos=float(input("Ingrese cantidad monetaria de dracmas griegos:"))
pesetas=float(input("Ingrese cantidad monetaria de pesetas:"))
#Caja negra
pesetas1=chelines_austriacos*9.56871
francos_franceses=dracmas_griegos*0.88607
francos_franceses2=francos_franceses/20.110
pesetas2=pesetas/122.499
libras=pesetas/0.09289
#Salidas
print("La conevrsion de austriacos a pesetas es:", pesetas1)
print("La conversion de dracmas a francos francese es:", francos_franceses2)
print("La cinversion de pesetas a dolares es:", pesetas2)
print("La conversion de pesetas a Libras italianas es:", libras)