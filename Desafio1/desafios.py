
print('Coleta e amostragem de dados')
#Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”

nome = input("Digite seu nome: ")
print("Olá, " + nome + "!");

#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("Olá, " + nome + ", você tem " + str(idade) + " anos.");

#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
print("Olá, " + nome + ", você tem " + str(idade) + " anos e mede " + str(altura) + " metros!");

print('Calculadora com operadores')

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
soma = valor1 + valor2
print("A soma dos valores é: " + str(soma));

#Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
soma = valor1 + valor2 + valor3
print("A soma dos valores é: " + str(soma));

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
subtracao = valor1 - valor2
print("A subtração dos valores é: " + str(subtracao));

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
multiplicacao = valor1 * valor2
print("A multiplicação dos valores é: " + str(multiplicacao));

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0
numerador = int(input("Digite o numerador: "))
denominador = int(input("Digite o denominador: "))
if denominador == 0:
    print("O denominador não pode ser 0.")
else:
    divisao = numerador / denominador
    print("A divisão dos valores é: " + str(divisao));  

#Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
exponeciacao = valor1 ** valor2
print("A exponenciação dos valores é: " + str(exponeciacao));

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input("Digite o numerador: "))
denominador = int(input("Digite o denominador: "))
if denominador == 0:
    print("O denominador não pode ser 0.")
else:
    divisao_inteira = numerador // denominador
    print("A divisão inteira dos valores é: " + str(divisao_inteira));  

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input("Digite o numerador: "))
denominador = int(input("Digite o denominador: "))
if denominador == 0:
    print("O denominador não pode ser 0.")
else:
    resto_divisao = numerador % denominador
    print("O resto da divisão dos valores é: " + str(resto_divisao));

#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
mediaArrendodada = round(media, 2)
print(f"A média das notas é: {mediaArrendodada:.2f}")

#Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
mediaPonderada = (5*1 + 12*2 + 20*3 + 15*4) / (1 + 2 + 3 + 4)
mediaPonderadaArrendodada = round(mediaPonderada, 2)
print(f"A média ponderada dos números é: {mediaPonderadaArrendodada:.2f}")

print('Editando textos');

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = 'Python é uma linguagem de programação'
print(frase)

#Crie um código que solicite uma frase e depois imprima a frase na tela.
digiteFrase = input("Digite uma frase: ")
print(digiteFrase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
fraseMaiscula = input("Digite uma frase: ")
print(fraseMaiscula.upper())

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
fraseMinuscula = input("Digite uma frase: ")
print(fraseMinuscula.lower())

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = '   Python é uma linguagem de programação     '
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase = input("Digite uma frase: ")
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input("Digite uma frase: ")
print(frase.strip().lower())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = input("Digite uma frase: ")
print(frase.replace('e','f'))

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input("Digite uma frase: ")
print(frase.replace('a', '@'))

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input("Digite uma frase: ")
print(frase.replace('s', '$'))

print('Fim dos desafios')