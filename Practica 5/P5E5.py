#P5E5 JAVIER DURAN Imprime un rectangulo con las medidas introducidas

ancho=int(input("Introduce la anchura del rectangulo: "))
altura=int(input("Introduce la altura del rectangulo: "))

for a in range(0,altura):
    print("{}".format("*"*(ancho)))