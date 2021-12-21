numero = input("Número entre 0 a 9999: ")
numero = " ".join(numero)
numero = numero.split()

print("Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}".format(numero[0],numero[1],numero[2],numero[3]))