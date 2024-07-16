n1, n2, n3 = input('Notas: ').split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 < n2 and n1 < n3:
    media = (n2 + n3) / 2
elif n2 < n3 and n2 < n1:
    media = (n1 + n3) / 2
else:
    media = (n1 + n2) / 2

if (media >= 90):
    conceito = 'A'
elif (media >= 80 ):
    conceito = 'B'
elif (media >= 60):
    conceito = 'C'
elif (media >= 40):
    conceito = 'D'
else:
    conceito = 'E'

print ('Conceito:', conceito)
if (media >= 60):
    print ('APROVADO')
else:
    print ('REPROVADO')    