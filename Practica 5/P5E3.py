#P5E3 JAVIER DURAN Pide dos numeros y imprime el sumatorio de todos los numeros intermedios

a, b=map(int,input("Introduce dos numeros: ").strip().split())
print("La suma de todos los numeros intermedios es {}.".format(sum(range(min(a,b), max(a,b)+1))))