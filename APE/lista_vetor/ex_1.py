n = int(input('N: '))
vetor_A = [0] * n
vetor_B = [0] * n

for i in range (n):
    vetor_A[i] = int(input('Valor: '))
k = int(input('K: '))
for i in range (n):
    vetor_B[i] = vetor_A[i] * k
print(vetor_A)
print(vetor_B)    