#P5E7 JAVIER DURAN Imprime un triangulo inverso dada la altura

altura=int(input("Introduce la altura del triangulo inverso: "))

for a in reversed(range(0,altura+1)):
    print("{}".format("*"*(a),altura*2-1))   