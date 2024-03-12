peso = float(input('Digite seu peso: '))
altura =float(input('Digite sua altura:'))
imc = peso / (altura**2)
if imc < 18.5:
    grau = 'baixo peso'
else:
    if imc < 25:
        grau = 'Normal'
    else:
        if imc < 30:
            grau = 'Sobrepeso'
        else:
            grau = 'obesidade'
print (grau)                        
