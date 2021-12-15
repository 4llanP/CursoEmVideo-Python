from math import hypot

print("="*48)

cateto = float(input("Cateto: "))
catetoAD = float(input("Cateto adjacente: "))

print("{:.0f}² + {:.0f}² = {:.0f}".format(cateto,catetoAD,hypot(cateto,catetoAD)))

print("="*48)