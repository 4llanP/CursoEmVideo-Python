print("="*48)

n = int(input("I will make one times tables for u, enter with a number: "))
x = 1
print("="*48)
for x in range(1,11):
    print("{:^1} x{:>3} = {:<}".format(n,x, n*x))
    x +=1

print("="*48)