nome = input("Seu nome: ").strip()

print("Seu nome em maiusculas é: {}".format(nome.upper()))
print("Seu nome em minusculas é: {}".format(nome.lower()))

print("Seu nome tem ao todo {} letras".format(len(nome)-1))

nome = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(nome[0],len(nome[0])))

19+4+7