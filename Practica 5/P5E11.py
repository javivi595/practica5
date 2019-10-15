#P5E11 JAVIER DURAN Imprime los divisores del numero introducido

num=int(input("Introduce un numero para saber todos sus divisores: "))
divisores=""
for a in range(1,num):
    if num%a==0:
        divisores+=str(a)+" "
print("El numero {} tiene como divisores: {}".format(num,divisores))
