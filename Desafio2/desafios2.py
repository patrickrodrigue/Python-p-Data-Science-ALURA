# Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O número maior é: ' + str(num1));
else:
    print('O número maior é: ' + str(num2));

# Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
crescimento = float(input('Digite o percentual de crscimento de produção da empresa: '))
ano2024 = 35
ano = 2025
diferenca = crescimento - ano2024
prejuizo = crescimento - ano2024
if crescimento == ano2024:
    print(f'Não houve crescimento de produção no ano de {ano}.')
elif crescimento > ano2024:
    print(f'Crescimento de produção no ano de {ano} foi de {diferenca}%.')
else:
    print(f'A empresa no ano de {ano} teve o prejuizo de {prejuizo}% .');

# Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input('Digite uma letra: ')
if letra in 'aeiou':
    print('A letra é uma vogal.')
else:    
    print('A letra é uma consoante.')

# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
modeloVeiculo1 = input('Digite o modelo do veículo: ')
precoVeiculo1 = float(input('Digite o preço médio do veículo: '))
modeloVeiculo2 = input('Digite o modelo do veículo: ')
precoVeiculo2 = float(input('Digite o preço médio do veículo: '))
modeloVeiculo3 = input('Digite o modelo do veículo: ')
precoVeiculo3 = float(input('Digite o preço médio do veículo: '))

precoMaximo = max(precoVeiculo1, precoVeiculo2, precoVeiculo3)
precoMinimo = min(precoVeiculo1, precoVeiculo2, precoVeiculo3)

if precoMaximo == precoVeiculo1:
    modeloMax = modeloVeiculo1
elif precoMaximo == precoVeiculo2:
    modeloMax = modeloVeiculo2
else:
    modeloMax = modeloVeiculo3

if precoMinimo == precoVeiculo1:
    modeloMin = modeloVeiculo1
elif precoMinimo == precoVeiculo2:
    modeloMin = modeloVeiculo2
else:
    modeloMin = modeloVeiculo3

print(f'O veículo mais caro é o {modeloMax} com o preço de R${precoMaximo} e o veículo mais barato é o {modeloMin} com o preço de R${precoMinimo}.')

# Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = input('Digite o nome do produto: ')
preco1 = float(input('Digite o preço do produto: '))
produto2 = input('Digite o nome do produto: ')
preco2 = float(input('Digite o preço do produto: '))
produto3 = input('Digite o nome do produto: ')
preco3 = float(input('Digite o preço do produto: '))

produtoBarato = min(preco1, preco2, preco3)

print(f'O produto mais barato é o {produtoBarato} com o preço de R${produtoBarato}.')

# Escreva um programa que leia três números e os exiba em ordem decrescente.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print(f'Os números em ordem decrescente são: {numeros}')

# Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
turno = input('Qual Turno você estuda?')
if turno == 'Manhã':
    print('Bom Dia!')
elif turno == 'Tarde':
    print('Boa Tarde!')
elif turno == 'Noite':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

# Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numero = int(input('Digite um numero:'))

if numero % 2 == 0 :
    print(f'O numero {numero} é par.')
else:
    print(f'O numero {numero} é impar.')

# Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

num = float(input('Digite um número: '))
resto = num % 1
if resto == 0:
    print(f'O número {num} é inteiro.')
else:
    print(f'O número {num} é decimal.')

# Momento dos projetos
print('Momento dos projetos')

# Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
operacao = input('Deseja receber a 1-soma, 2-subtração, 3-divisão, 4-resto da divisão ou 5-multiplicação?')

if operacao in '1':
    resultado = num1 + num2
    print(f'O resultado da soma é {resultado}')
elif operacao in '2':
    resultado = num1 - num2
    print(f'O resultado da subtração é {resultado}')
elif operacao in '3':
    resultado = num1 / num2 
    print(f'O resultado da divisão é {resultado}')
elif operacao in '4':
    resultado = num1 % num2
    print(f'O resto da divisão é {resultado}')
elif operacao in '5':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é {resultado}')
else:
    print('Operação inválida.')

if resultado % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')

if resultado >= 0:
    print('O número é positivo.')
elif resultado < 0:
    print('O número é negativo.')

if resultado % 1 == 0:
    print('O número é inteiro.')
else:
    print('O número é decimal.')

# Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.
lado1 = float(input('Digite o valor do primeiro lado do seu triângulo: '))
lado2 =  float(input('Digite o valor do segundo lado do seu triângulo: '))
lado3 =  float(input('Digite o valor do terceiro lado do seu triângulo: '))
sum1 = lado1 + lado2
sum2 = lado1 + lado3
sum3 = lado2 + lado3
if sum1 > lado3:
 print('É um triângulo')
elif sum2 > lado2:
 print('É um triângulo')
elif sum3 > lado1:
    print('É um triângulo')
else:
    print('Não é um triângulo')

if lado1 == lado2 == lado3:
    print('Triângulo Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo Isósceles')
if lado1 != lado2 != lado3:
    print('Triângulo Escaleno')


#Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
tipo = input('Qual combustível foi vendido? 1-Etanol, 2-Diesel:')
litros = float(input('Quantos litros foram vendidos?'))
precoDiesel = 2.00
precoEtanol = 1.70
descontoEtanol1 = 0.02 #até 15L
descontoEtanol2 = 0.04 #acima de 15L
descontoDiesel1 = 0.03 #até 15L
descontoDiesel2 = 0.05 #acima de 15L

if tipo == "1":
    if litros <= 15:
        desconto = (descontoEtanol1 * litros * precoEtanol)
        valoraPagar = (litros * precoEtanol) - desconto
        print(f'O valor a pagar pelo etanol é  R${valoraPagar}')
    else:
        desconto = (descontoEtanol2 * litros * precoEtanol)
        valoraPagar = (litros * precoEtanol) - desconto
        print(f'O valor a pagar pelo etanol é R${valoraPagar}')

elif tipo == "2":
    if litros <= 15:
        desconto = (descontoDiesel1 * litros * precoDiesel)
        valoraPagar = (litros * precoDiesel) - desconto
        print(f'O valor a pagar pelo diesel é R${valoraPagar}')
    else:
        desconto = (descontoDiesel2 * litros * precoDiesel)
        valoraPagar = (litros * precoDiesel) - desconto
        print(f'O valor a pagar pelo diesel é R${valoraPagar}')
else:
    print("Opção inválida! Escolha 1 para Etanol ou 2 para Diesel.")

# Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para bonificações abaixo de -10%: corte de gastos.

vendas2022 = float(input('Digite o valor de vendas em 2022: '))
vendas2023 = float(input('Digite o valor de vendas em 2023: '))
variacaoPercentual = ((vendas2023 - vendas2022) / vendas2022) * 100

if variacaoPercentual > 20:
    print('Bonificação para o time de vendas.')
elif variacaoPercentual >= 2 and variacaoPercentual <= 20:
    print('Pequena bonificação para o time de vendas.')
elif variacaoPercentual >= -10 and variacaoPercentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
elif variacaoPercentual < -10:
    print('Corte de gastos.')
else:
    print('Variação não identificada.')

print('Fim dos projetos')