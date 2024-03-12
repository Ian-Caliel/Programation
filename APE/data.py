data = input('Informe a validade: ')
dia, mes, ano =  data.split('/')
dia,mes,ano = int(dia), int(mes), int(ano)
print(dia,mes,ano) 
if ano> 2024:
    print ('Compre')
else:
    if ano < 2024:
        print('reclame')
    else:
        if (mes > 3):
            print ('compre')
        else:
            if mes < 3:
                print ('reclame')
            else:
                if dia>=7:
                    print ('compre')
                else:
                    if dia<7:
                        print ('reclame')                            
