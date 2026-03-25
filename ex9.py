
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
