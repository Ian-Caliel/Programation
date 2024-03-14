caracter = input('digite um caractere: ')
if caracter in '1234567890':
    print('Numeros')
elif caracter in "!@#$%¨&*(){<}>:;?/|-+=_":
    print('especial')    
elif caracter.lower() in 'aeiou':
    print('Vogais')
elif caracter.lower() in 'inqwrtypsdfghjklmnbvcxzç':
    print('consoante')
else:
    print('Toma no cu')    