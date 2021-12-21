frase = "curso em video python"

    #FATIAMENTO:

print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[15:])
print(frase[:5])
print(frase[::2])
print(frase[9::3])
#[posição inicial de exibição, posição final de exibição(se 14 aparece posição 13), numero de passos]

    #ANÁLISE:

print(len(frase))
#Tamanho

print(frase.count("o"))
print(frase.count("o",0,13))
#Contador, A != a

print(frase.find("deo"))
#Onde começa oq foi procurado "deo" no caso, casa 11 (conta espaços)

print("curso" in frase)
#Boleana se existe ou não existe

    #TRANSFORMAÇÃO:

print(frase.replace("python","Android"))
#Substitui textos (tem que estar escrito igual o texto)

print(frase.upper())
#DEIXA TUDO EM MAIUSCULO
print(frase.lower())
#deixa tudo em minusculo
print(frase.capitalize())
#Deixa a primeira letra em maiuscula
print(frase.title())
#Deixa Todas As Primeiras Letras Após O Espaço Maiusculas

frase = "     Aprenda python        "

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
#Strip corta espaços antes e depois de palavas, Prefixo L corta só da esquerda, Prefixo R corta só o da direita

    #DIVISÃO

frase = "curso em video python"

print(frase.split())
#Separa a frase nos espaços, formando uma lista

    #JUNÇÃO

print('_'.join(frase))
#Separa as letras pelo oq for definido no ""
print('@'.join(frase.split()))
#Caso split tenha separado ele junta