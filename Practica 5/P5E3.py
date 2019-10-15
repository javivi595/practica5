#P5E3 JAVIER DURAN Pide dos numeros y imprime el sumatorio de todos los numeros intermedios

#Forma rapida
#a, b=map(int,input("Introduce dos numeros: ").strip().split())
#print("La suma de todos los numeros intermedios es {}.".format(sum(range(min(a,b), max(a,b)+1))))

#Forma con for

a, b=map(int,input("Introduce dos numeros para hacer sumatorio de su rango: ").strip().split())
suma=0

if a<b:
    for c in range(a,b+1):
        suma+=c
else:
    for c in range(b,a+1):
        suma+=c
print("El sumatorio total es", suma)
