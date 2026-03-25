s = input("Digite uma frase: (No mínimo 6 caracteres)")

if len(s) < 6:
    print("Precisa ser maior ou igual a 6 caracteres!!")
else:
    print("O primeiro caracter: ", s[0])
    print("O tres primeiros caracter: ", s[:3])
    print("O tres ultimos caracter: ", s[-3:])
    print("O texto sem o primeiro caracter: ", s[1:])
    print("O texto sem o ultimo caracter: ", s[:-1])