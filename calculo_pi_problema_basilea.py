import math
six=6
N=input("Ingrese el numero de iteraciones con el que desea encontrar el valor de pi=> ")
s=0
for i in range(0,N):
    s=(1/(math.pow(1+i,2)))+s

pi=math.sqrt(six*s)
#print(s)
print(pi)
