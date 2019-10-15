#P5E10 JAVIER DURAN Imprime un triangulo centrado

altura=int(input("Introduce la altura del triangulo: "))

for a in range(0,altura*2):
    if a%2==1:
        print("{:^{}}".format("*"*(a),altura*2-1))
       