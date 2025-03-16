#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
for i in range(num1, num2+1):
    print(i)

#Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
bacteriaA = 4
bacteriaB = 10
crecimentoA = 1.03
crecimentoB = 1.015
dia = 1

while bacteriaA <= bacteriaB:
    bacteriaA *= crecimentoA
    bacteriaB *= crecimentoB
    
    dia = dia + 1
    
print(f'{dia} dias')

#Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
contador = 1
totalDeNotas = 0
while contador <= 15:
    nota = float(input('Digite uma nota:'))
    
    if nota >= 0 and nota <=5:
        print(nota)
        contador += 1
        totalDeNotas += 1
    else:
        print('Nota inválida, digite novamente')
print(f'Total de {totalDeNotas} notas coletadas')

# Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
contador = 0
soma = 0
temperatura = float(input('Informe os valores de temperatura em Celsius (Media valores ja digitados escreva "-273"):  '))

while temperatura != -273:
    soma += temperatura
    contador += 1
    temperatura = float(input('Informe os valores de temperatura em Celsius (Media valores ja digitados escreva "-273"):  '))
    media = soma/contador

print(f'A media das temperaturas e {media:.1f}')

#5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
num = int(input('Digite um número para descobrir seu fatorial:'))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f'O fatorial de {num} é {fatorial}')

print('Momento dos Projetos')

#Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária: 
numTabuada = int(input('Digite um numero para saber sua tabuada:'))
contador = 0

for i in range(  1 , 11):
    i *= numTabuada
    contador += 1
    print(f'{numTabuada} x {contador} = {i}')