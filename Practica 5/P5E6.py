#P5E6 JAVIER DURAN Imprime un triangulo con la altura dada

altura=int(input("Introduce la altura del triangulo: "))

for a in range(0,altura+1):
    print("{}".format("*"*(a),altura*2-1))
       