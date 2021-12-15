from random import shuffle

print("="*48)

n1 = input("Student: ")
n2 = input("Student: ")
n3 = input("Student: ")
n4 = input("Student: ")

print("\n="+"="*47)

alunos = [n1,n2,n3,n4]
shuffle(alunos)

print("\nOrder: \n1º: {}\n2º: {}\n3º: {}\n4º: {}\n".format(alunos[0],alunos[1],alunos[2],alunos[3],))

print("="*48)
