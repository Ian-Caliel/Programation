import random
numeros = [0] * 10
for i in range(len(numeros)):
    numeros[i] = (i + 1) * 10

for i in range(10):
    if (i % 2 == 0):
        print(numeros[i])
for i in range(0, 10, 2):
    print(numeros[i])
for i in range(1, 10, 2):
    print(numeros[i])