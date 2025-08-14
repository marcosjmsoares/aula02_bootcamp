# Inteiros (int)
# 1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# val1 = int(input("Insira um valor:"))
# val2 = int(input("Insira um valor:"))
# soma = val1+val2
# print("Soma é igual a " + str(soma))

# 2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# divisor=5
# valor1= int(input("Insira um numero: "))
# calculo = valor1 % divisor
# print("O resto da divisão é: " + str(calculo))

# 3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# valor1=int(input("Insira um valor: "))
# valor2=int(input("Insira outro valor: "))
# calculo = valor1 * valor2
# print("O resultado é: " + str(calculo))

# 4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# valor1=int(input("Insira um valor: "))
# valor2=int(input("Insira outro valor: "))
# calculo = int(valor1/valor2)
# print("O valor da divisão é " + str(calculo))

# 5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# valor=int(input("Insira um valor: "))
# calculo= valor*valor
# print("O resultado do quadrado do número fornecido é " + str(calculo))

# Números de Ponto Flutuante (float)
# 6-Escreva um programa que receba dois números flutuantes e realize sua adição.
# valor1=float(input("Insira um valor: "))
# valor2=float(input("Insira um valor: "))
# print("A soma é " + str(valor1+valor2))

# 7-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário
# valor1=float(input("Insira um valor: "))
# valor2=float(input("Insira um valor: "))
# calculo = (valor1+valor2)/2
# print("A média dos valores é de " , (calculo), ". Obrigado por perguntar!")

# 8-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
# potencia = base ** expoente
# print("O resultado da potência é:", potencia)

# 9-Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o raio do círculo: "))
# area = 3.14159 * raio ** 2
# print("A área do círculo é:", area)

# Strings (str)
# 11-Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = str(input("Insira um texto minusculo: "))
# texto_maiusculo = texto.upper()
# print(f"Texto em maiusculo: {texto_maiusculo}")

# 12-Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# texto = str(input("Insira um texto maiusculo: "))
# texto_minusculo = texto.lower()
# print(f"Texto em minusculo: {texto_minusculo}")

# 13-Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco 
# no início e no final.
# texto = input("Insira um texto: ")
# ajuste = texto.strip()
# print(f"Frase sem espaço no incio e fim: {ajuste}")

# 14-Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, 
# o mês e o ano separadamente.
# data = input("Digite uma data no formato dd/mm/aaaa")
# dia, mes, ano, hora= data.split("/")
# print(dia, mes, ano, hora)

# 15-Escreva um programa que concatene duas strings fornecidas pelo usuário.
# texto1=input("Digite uma frase: ")
# texto2=input("Digite uma frase: ")
# concatenar = texto1 + texto2
# print(f"A concatenação das duas frases é: {concatenar}")

# Booleanos (bool)
# 16-Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = True
# valor2 = False
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)

# 17-Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# valor1 = bool(input("Insira um valor booleano: "))
# valor2 = bool(input("Insira outro valor booleano: "))
# resultado = valor1 or valor2
# print(f"O resultado dos booleanos é: {resultado}")

# 18-Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor1 = bool(input("Insira um valor booleano: "))
# resultado_not = not valor1
# print("Resultado do NOT lógico:", resultado_not)

# 19-Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# valor1 = int(input("Insira um numero: "))
# valor2 = int(input("Insira um numero: "))
# comparacao = valor1 == valor2
# print(f"Resultado se os valores informados são iguais: {comparacao}")

# 20-Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1 = int(input("Insira um numero: "))
# valor2 = int(input("Insira um numero: "))
# comparacao = valor1 !=  valor2
# print(f"Resultado se os valores informados são diferentes: {comparacao}")


# Try Except / IF
# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.