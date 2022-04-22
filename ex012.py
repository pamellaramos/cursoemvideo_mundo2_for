#Contagem de pares
#mostra todos os número pares entre 1 e 50

pares = []
for i in range(1,51):
    if i % 2 == 0:
        pares.append(i)

print(pares)