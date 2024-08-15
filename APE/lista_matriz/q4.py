import random

matriz = [0] * 20

# Preencher matriz
soma_medias = 0
for i in range(20):
    notas = [random.randint(0,100) for _ in range(3)] + [0]
    media = round((sum(notas) / 3), 1)
    notas[3] = media
    soma_medias += media
    matriz[i] = notas

media_geral = round((soma_medias / 20), 1)
acima_media = 0

# Checar alunas acima da media
for i in range(20):
    if matriz[i][-1] > media_geral:
        acima_media += 1

# Exibir matriz
print("[Nota1,Nota2,Nota3,Media]")
print(*matriz, sep='\n')
print("Media geral:", media_geral)
print("Alunos acima da media:", acima_media)