frequencia = int(input('frequencia: '))
if (frequencia >= 75):
     nota1 = int(input('nota1: '))
     nota2 = int(input('nota2: '))
     media = (nota1 + nota2) / 2
     print (f'media = {media:.2f}')
     if (media>=70):
          print ('Aprovado')
     else:
          if (media >= 40):
               print ('final')
          else:
               print ('Reprovado por media')          
else:
     print('Reprovado por falta')
     


 

