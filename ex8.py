n = int(input("Digite um numero inteiro: "))

print("Equacao 1: ", n % 2 == 0)
# Essa equação mostra se o numero é par
print("Equacao 2:", n % 3 == 0)
# Ja essa mostra se o numero é ímpar
print("Equacao 3: ", (n % 2 == 0) and (n % 3 == 0))
# E essa equação verifica se é par e ímpar ao mesmo tempo

