qt_F = 0
qt_FSI20 = 0
at_HCM30 = 0
for i in range (4):
    idade = int(input('idade: '))
    sexo = input('Sexo, M ou F: ')
    estado = input('Estado Civil (s/c/v/d): ')

    if sexo == 'F':
        qt_F += 1 
    if sexo == 'F' and estado == 's' and idade < 20:
        qt_FSI20 += 1
    if sexo == 'M' and estado == 'c' and idade > 30:
        at_HCM30 += 1
print (f'O percentual de mulheres: {qt_F}%')
print (f'O percentual de homens: {100-qt_F}%')
print (f'Mulheres solteiras com idade inferior a 20: {qt_FSI20}')
print (f'Homens casados com mais de 30: {at_HCM30}')
