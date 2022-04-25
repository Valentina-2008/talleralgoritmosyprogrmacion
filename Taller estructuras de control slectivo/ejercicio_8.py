#Entrada
p=int(input("Ingrese el valor de P:"))
q=int(input("Ingrese el valor de Q:"))
#caja negra
o=p**3+q**4-2*(p**2)
r=""
if(o>680):
    r="satisfacen la expresión"
else:
    r="no Satisfacen la expresión"
#salida
print(f"{p} y {q} {r}")