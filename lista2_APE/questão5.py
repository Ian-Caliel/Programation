segundos = int(input('Segundos: '))
horas = (segundos // 3600)
resto = segundos % 3600
minutos = resto // 60
segundos_final = resto % 60
print (f'{horas} Horas,  {minutos} minutos,  {segundos_final} segundos.')