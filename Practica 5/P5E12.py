#P5E12 JAVIER DURAN Imprime si el numero introducido es primo

num=int(input("Introduce un numero para saber si es primo: "))
divisores=0
for a in range(2,num):
    if num%a==0:
        divisores+=1
if divisores==0:
    print("El numero {} es primo.".format(num))
else:
    print("El numero {} no es primo.".format(num))
