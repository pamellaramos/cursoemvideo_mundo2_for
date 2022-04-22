#Soma impares multiplos de três
#que se encontram entre 1 e 500
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        #contador
        cont = cont + 1
        #acumulador
        soma = soma + i

print(soma)
print(cont)

