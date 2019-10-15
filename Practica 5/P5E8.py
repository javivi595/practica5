#P5E8 JAVIER DURAN Imprime como un rombo-triangulo dada la altura

altura=int(input("Introduce la altura del triangulo: "))

for a in range(0,altura+1):
    print("{}".format("*"*(a),altura*2-1))
for a in reversed(range(0,altura)):
    print("{}".format("*"*(a),altura*2-1))  