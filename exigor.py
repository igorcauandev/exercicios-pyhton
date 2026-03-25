# ------ 1 / Primeiro Exercicio ------
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))

print(f"Nome: {nome} | Idade aproximada: {2026 - ano_nascimento} anos")

# ----- 2 / Segundo Exercício ------
s = input("Digite qualquer coisa: ")

print("Conteudo digitado: ", s)
print(type(s))
print(len(s))

# ------ 3 / Terceiro Exercício ------


# ------ 4 / Quarto Exercício ------
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

print(f"A base e:  {base:.2f} | A altura e: {altura:.2f}")

# ------ 5 / Quinto Exercício ------
a = int(input("Digite o numero a: "))
b = int(input("Digite o numero B: "))
c = int(input("Digite o numero C: "))

e1 = a + (b * c)
e2 = (a + b) * c
e3 = (a ** 2) + (b ** 2) + (c ** 2)

print("O calculo de E1 = a + b · c é: ", e1)
print("O calculo de E2 = (a + b) · c é: ", e2)
print("O calculo de E1 = a2+b2+c2 é: ", e3)

# ------ 6 / Sexto Exercício ------
valor = int(input("Digite um valor em metros:"))

centimetros = valor / 100
milimetros = valor / 1000

print('Valor em centimetros: ', centimetros)
print("Valor em milimetros: ", milimetros)

# ------ 7 / Sétimo Exercício ------
tempC = float(input("Digite a temperatura em Celcius: "))
tempF = (1.8 * tempC) + 32
print("A temperatura convertida para Fahrenheit e: ", tempF)

Tempf = float(input("Digite uma temperatura em Fareheint: "))
Tempc = (Tempf - 32) / 1.8
print("A temperatura convertida para Celcius e: ", Tempc)

# ------ 8 / Oitavo Exercício ------
n = int(input("Digite um numero inteiro: "))

print("Equacao 1: ", n % 2 == 0)
# Essa equação mostra se o numero é par
print("Equacao 2:", n % 3 == 0)
# Ja essa mostra se o numero é ímpar
print("Equacao 3: ", (n % 2 == 0) and (n % 3 == 0))
# E essa equação verifica se é par e ímpar ao mesmo tempo

# ------ 9 / Nono Exercício ------

print('-- Calcule sua média ponderada -- ')

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

print('-- Agora digite os pesos -- ')

p1 = float(input("Peso da nota um: "))
p2 = float(input("Peso da nota dois: "))
p3 = float(input("Peso da nota tres: "))

notaponderada = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
print("Sua nota ponderada e:", notaponderada)

# ------ 10 / Décimo Exercício ------
