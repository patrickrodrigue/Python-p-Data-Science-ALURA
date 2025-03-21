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
lista_1 = []
contador = 1
while contador < 6:
    lista_1.append(int(input('Digite um número:')))
    contador += 1
print(lista_1)

#  Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista_inversa = []
cont = 1
for i in range(cont, 6):
    lista_inversa.append(int(input('Digite um número:')))
    i+=1
lista_inversa.sort(reverse = True)# Ou print(lista_inversa[::-1])
print(lista_inversa)

#Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
num = int(input('Informe um numero: '))
lista_primos = []

for intervalo in range(2,num):
    primo = True
    for teste_primo in range(2,intervalo):
        if intervalo%teste_primo == 0:
          primo = False
          break
    if primo:
      lista_primos.append(intervalo)

print(f'os numeros primos são{lista_primos}')

#Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
dia = int(input('Digite o dia:'))
mes = int(input('Digite o mês:'))
ano = int(input('Digite o ano:'))
mes_ate_31 = (1, 3, 5, 7, 8, 10,12)
mes_ate_30 = (4, 6, 9, 11)
data = False

if mes in mes_ate_31:
    if dia <= 31:
        data = True
elif mes in mes_ate_30:
    if dia <= 30:
        data = True
elif mes == 2:
    if(ano % 4 == 0 and ano%100 != 0) or (ano%400 == 0):
        if dia <= 29:
          data =True
        elif dia <= 28:
           data = True
if(data):
    print('Data Válida')
else:
    print('Data Inválida')

print('MOMENTO DOS PROJETOS')

# Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
numeros_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crescimento = []
for i in range(1, len(numeros_bacterias)):
    calculo = 100*(numeros_bacterias[i] - numeros_bacterias [i - 1])/ numeros_bacterias[i - 1]
    crescimento.append(calculo)
for i, crescimento in enumerate(crescimento,start=1):
    print(f'Crescimento do dia {i}: {crescimento:.2f}%')

#Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
doces = 0
amargos = 0 
for i in range(1, 11):
    ids = int(input('Digite o id:'))
    if ids % 2 == 0:
        doces+=1
    else:
        amargos+=1
print(f'Total de doces amargos são {amargos} é de doces são {doces}')

#Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C','C', 'A', 'B']
nota = 0
respostas = []
for i in range(10):
    i = input(f'Digite a resposta da questão {i+1}:').upper()
    respostas.append(i)
for i in range(10):
    if respostas[i] == gabarito[i]:
        nota+=1
    
print(f'a nota do(a) aluno foi {nota}')

#Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatua_media = []
for i in range (12):
    i = float(input(f'Informe a temperatura media do mes {i+1}: '))
    temperatua_media.append(i)
    media=sum(temperatua_media)/len(temperatua_media)
for i in range(12):
    if temperatua_media[i] > media:
        print(f'Os meses foram {mes[i]}')

#Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
#{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 #'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
#Escreva um código que calcule o total de vendas e o produto mais vendido.
vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 
          'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total = 0
produto_mais_vendido = ''
produtos_vendidos = 0

for i in vendas.keys():
    total += vendas[i]
    if vendas[i] > produtos_vendidos:
        produtos_vendidos = vendas[i]
        produto_mais_vendido = i
print(f'O total de vendas: {total}')
print(f'O produto mais vendido: {produto_mais_vendido}')

# Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:
# Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos
#Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
votos = {'Design 1': 1334, 'Design 2':982, 'Design 3':1751, 'Design 4':210, 'Design 5': 1811}
votos_total = 0
desing = ''
quntidade_vts = 0
percentual = 0

for i in votos.keys():
    votos_total += votos[i]
    if votos[i] > quntidade_vts:
        quntidade_vts = votos[i]
        desing = i
        percentual = (quntidade_vts/votos_total)*100
print(f'O {desing} venceu com {percentual:.2f}% de votos')

# As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {salario:max(salario*0.1,200) for salario in salarios}
total_abono = sum(abonos.values())
abono_minimo = sum(1 for abono in abonos.values() if abono == 200)
maior_abono = max(abonos.values())

print("Dicionário de abonos:", abonos)
print(f'Total gasto com abonos: {total_abono}')
print(f'Colaboradores que receberam o abono mínimo: {abono_minimo:.2f}')
print(f'Maior valor de abono fornecido: {maior_abono:.2f}')

# Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
# {'Área Norte': [2819, 7236],
#  'Área Leste': [1440, 9492],
#  'Área Sul': [5969, 7496],
#  'Área Oeste': [14446, 49688],
#  'Área Centro': [22558, 45148]}
# Copiar código
# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
areas = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

medias = {area:sum(especies)/len(especies) for area, especies in areas.items()}
maior_diversidade = max(medias, key=medias.get)

print(f'Media de espécie por area: {medias}\n Área com maior divercidade: {maior_diversidade}')

# O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Copiar código
# Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
dados = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

medias_setores = {setor: sum(idades) / len(idades) for setor, idades in dados.items()}
idades_geral = [idade for idades in dados.values() for idade in idades]
media_geral = sum(idades_geral)/ len(idades_geral)
acima = sum(1 for idade in idades_geral if idade > media_geral)

print("Média de idade por setor:")
for setor, media in medias_setores.items():
    print(f"{setor}: {media:.2f} anos")

print(f"\nMédia de idade geral: {media_geral:.2f} anos")
print(f"Número de colaboradores acima da média geral: {acima}")