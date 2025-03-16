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

# Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Digite um número: (0) para sair.'))

while num != 0:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f'{num} não é um número primo.')
                break
        else:
            print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.')
    
    num = int(input('Digite um número: (0) para sair.'))

#Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

faixa_0_a_25 = 0
faixa_26_a_50 = 0
faixa_51_a_75 = 0
faixa_76_a_100 = 0

while True:
    idade = int(input('Digite a idade(numero negativo para sair):'))

    if idade <0:
        break

    if 0 <= idade <= 25:
        faixa_0_a_25 += 1
    elif 26 <= idade <= 50:
        faixa_26_a_50 += 1
    elif 51 <= idade <=75:
        faixa_51_a_75 += 1
    elif 76 <= idade <= 100:
        faixa_76_a_100 += 1
    
print('\nDistribuição de idades:')
print(f'[0-25] anos:{faixa_0_a_25} ]')
print(f'[26-50] anos:{faixa_26_a_50} ]')
print(f'[51-75] anos:{faixa_51_a_75} ]')
print(f'[76-100] anos:{faixa_76_a_100} ]')

#Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
votos =[]
for i in range(1 , 21):
    voto = int(input(' 1- Candidato A\n 2- Candidato B\n 3- Candidato C\n 4- Candidato D\n 5- voto nulo\n 6- voto em branco\n Digite o seu voto:'))
    votos.append(voto)
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0
contador_6 = 0
for voto in votos:
    if voto == 1:
        contador_1 += 1
    elif voto == 2:
        contador_2 += 1
    elif voto == 3:
        contador_3 += 1
    elif voto == 4:
        contador_4 += 1
    elif voto == 5:
        contador_5 += 1
    elif voto == 6:
        contador_6 += 1

totalVotos = len(votos)
percentualNulo = (contador_5 / totalVotos)
percentualBranco = (contador_5 / totalVotos)

print(f"Resultado da votação:\n Candidato A = {contador_1}\nCandidato B = {contador_2}\nCandidato C = {contador_3}\nCandidato D = {contador_4}\nVotos Nulos = {contador_5}\nVotos em branco = {contador_6}")