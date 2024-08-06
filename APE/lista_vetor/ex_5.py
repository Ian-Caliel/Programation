import random
numeros = list(range(1,20,2))
random.shurffle(numeros)

menor_i = maior_i = 0 

for i in range(1,10):
    if (numeros[i] > numeros[maior_i]):
        maior_i = i
    else:
        menor_i = i

print(numeros[maior_i], maior_i)
print(numeros[menor_i], menor_i)

