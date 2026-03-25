valores = [True, False]

for p in valores:
    for q in valores:
        ex1 = not (p and q)
        print(p, q, ex1)


for p in valores:
    for q in valores:
        ex2 = (p or q) and not p
        print(p, q, ex2)

for p in valores:
    for q in valores:
        ex3 = (not p or q) and p
        print(p, q, ex3)

for p in valores:
    for q in valores:
        for r in valores:
            ex4 = not (p or q) or r
            print(p, q, ex4)