import random

numeros = [0] * 10
qt = 0

for i in range(len(numeros)):
    numeros[i] = random.randint(1,8)
k = int(input('Chute: '))
for i in range(len(numeros)):
    if (numeros[i] == k):
        qt += 1 
print(numeros)
print(qt)
