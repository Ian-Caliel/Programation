
import random

matriz_A = [0] * 2
matriz_B = [0] * 2
matriz_C = [0] * 2

for i in range(2):
    linha = [0] * 3
    for j in range(3):
        linha[j] = random.randint(1,9)
    matriz_A[i] = linha 

for i in range(2):
    linha = [0] * 3
    for j in range(3):
        linha[j] = random.randint(1,9)
    matriz_B[i] = linha 

for i in range(2):
    linha = [0] * 3
    matriz_C[i] = linha 

for i in range(2):
    for j in range(3):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

print('matriz_A')
for i in range(2):
    print(matriz_A[i])

print('\nmatriz_B')
for i in range(2):
    print(matriz_B[i])

print('\nmatriz_C')
for i in range(2):
    print(matriz_C[i])



