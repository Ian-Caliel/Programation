valor1, operacao, valor2 =  input('Expressão: ').split()
valor1, valor2 = float (valor1), float (valor2)
if operacao == '+':
    resultado = valor1 + valor2
    print (valor1, operacao, valor2, '=', resultado)
else:
    if operacao == '-':
        resultado = valor1 - valor2
        print (valor1, operacao, valor2, '=', resultado)
    else:
        if operacao == 'x':    
            resultado = valor1 * valor2
            print (valor1, operacao, valor2, '=', resultado)
        else:
            if operacao == '*':
                resultado = valor1 ** valor2
                print (valor1, operacao, valor2, '=', resultado)
            else:
                if operacao == '/':
                    resultado = valor1 / valor2
                    print (valor1, operacao, valor2, '=', resultado)
                else:
                    if operacao == '%':
                        resultado = valor1 % valor2
                        print (valor1, operacao, valor2, '=', resultado)            