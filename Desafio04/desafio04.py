#Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
quantidade = len(gastos)
media = sum(gastos)/quantidade
print(f'A media de gastos e {media:.2f}')

#Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
maiores_compras = 0 
for valores in gastos:
    if valores > 3000:
        maiores_compras += 1

porcentagem = (maiores_compras/quantidade)*100
print(f'Foi realizado {maiores_compras} compras acima de 3.000,00 reais, sendo {porcentagem:.2f}% da quantidade total de compras.')

#Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].