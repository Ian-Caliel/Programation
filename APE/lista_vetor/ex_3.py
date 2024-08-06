import random
n = int(input('N: '))
numeros = [0] * n
indices = []
for i in range(len(numeros)):
    numeros[i] = random.randint(1,8)
k = int(input('Chute: '))
for i in range(n):
    if (numeros[i] == k):
        indices.append(i)
if (len(indices) > 0):
    print('Achei: ', indices)
else:
    print('Não achei')
               