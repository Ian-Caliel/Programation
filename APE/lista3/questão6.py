nome = input('Digite seu nome: ')
recomendação = input('Digite sua recomendaão ( A, B, C ou D): ')
match recomendação.upper():
    case 'A':
        print(f'{nome}, fortemende recomendado')
    case 'B':
        print(f'{nome}, recomendado') 
    case 'C':
        print(f'{nome}, recomendado') 
    case 'D':
        print (f'{nome}, não recomendado')    
