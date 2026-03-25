
n = int(input("Digite o número de itens: "))
k = int(input("Digite o número de pessoas: "))

itens_por_pessoa = n // k
resto = n % k

print("Cada pessoa recebe:", itens_por_pessoa)
print("Sobram:", resto)