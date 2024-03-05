antes = int(input('Antes: '))
depois = int(input('depois: '))
litros = float(input('litros gastos: '))
valor_combus = float(input('Qual valor do combus: '))
capacidade =  int(input('Capacidade do tanque: '))
km_rodado = depois - antes
km_por_litro = km_rodado / litros
autonomia = capacidade * km_por_litro
custo = litros * valor_combus
print (f'Km rodada {km_rodado:.2f}')
print (f'eficiencia {km_por_litro:.2f}')
print (f'Autonomia {autonomia:.2f}')
print  (f'Custo da viagem {custo:.2f}')
