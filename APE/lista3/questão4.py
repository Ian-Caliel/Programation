nome = input('Digite seu nome: ')
sexo = input('Qual seu sexo? (M para masculino) (F para feminino): ')
if sexo == 'M' or sexo== 'm':
    print(f'Olá, Sr.{nome}')
else:
    print (f'Olá, Sra.{nome}')