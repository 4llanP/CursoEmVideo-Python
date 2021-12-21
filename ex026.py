frase = input("Frase: ").strip().lower()

print("A letra a, aparece:",frase.count("a"))
print("Primeira vez na casa:",frase.find("a")+1)
print("ultima vez na casa:",frase.rfind("a")+1)