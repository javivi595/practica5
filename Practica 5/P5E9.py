#P5E9 JAVIER DURAN Imprime un rectangulo bordeado

ancho=int(input("Introduce la anchura del rectangulo: "))
altura=int(input("Introduce la altura del rectangulo: "))

for a in range(0,altura):
    if a==0 or a==altura-1:
        print("{}".format("*"*(ancho)))
    else:
        print("*{}*".format(" "*(ancho-2)))
    