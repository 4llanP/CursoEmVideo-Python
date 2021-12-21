nome = input("Nome: ").strip().title()

print("nome: {}\nPrimeiro nome: {}\nUltimo nome: {}".format(nome, nome[0:nome.find(" ")], nome[nome.rfind(" ")+1:len(nome)]))

#nomes = nome.split()
#print("nome: {}\nPrimeiro nome: {}\nUltimo nome: {}".format(nome.title(),nomes[0].capitalize(),nomes.pop().capitalize()))