from typing import TextIO
maiscula = minuscula = numerico = especial = 0

texto = input('Texto: ')
for i in range (len(texto)):
    #print (i, texto[i], ord(texto[i]))#
    if (texto[i] >= 'A') and (texto[i] <= 'z'):
        maiscula += 1
    elif (texto[i] >= 'a') and (texto[i] <= 'z'):
        minuscula +=1
    elif (texto[i] >= '0') and (texto[i] <= '9'):
        numerico += 1
    else:
        especial += 1
print('Simbolos:', len(texto))
print('Letra: ',maiscula + minuscula)
print('Maiusculas:', maiscula)
print('Minuscula:', minuscula) 
print('Numericos:',numerico)
print('especiais:',especial)       