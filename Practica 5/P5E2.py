#P5E2 JAVIER DURAN Pedir dos numeros y decir que numeros pares y impares hay dentro de su rango.

a, b=map(int,input("Introduce dos numeros: ").strip().split())
for p in range(min(a,b),max(a,b)+1):
    if p%2==0:
        print("El numero {} es par".format(p))
    else:
        print("El numero {} es impar".format(p))