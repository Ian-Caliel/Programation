n = int(input())

vetorA = [int(input()) for _ in range(n)]
vetorB = [int(input()) for _ in range(n)]
vetorC = [0] * (n * 2)

for i in range (n * 2):
    vetorC[i] = vetorA[i]
    vetorC[i+1] = vetorB[i]


print(vetorA)
print(vetorB)
print(vetorC)    