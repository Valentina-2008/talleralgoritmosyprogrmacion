A=int(input("Digite valor de A"))
B=int(input("A dividido en:"))
c=0
while (A>1):
    if(A!=0 or A!=1):
        A=A-B
        c=c+1
    elif(A==0 or A==1):
        break
print(f"El cociente es: {c} y el resto es {A}")
