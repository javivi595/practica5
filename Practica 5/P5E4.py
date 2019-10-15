#P5E4 JAVIER DURAN Imprime el factorial del numero introducido

fact=int(input("Introduce un numero para factorizar: "))
for a in reversed(range(1,fact)):
    fact*=a
print("El numero factorizado es:",fact)