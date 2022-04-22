#Soma dos pares

lista = []
for i in range(1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        lista.append(num)
soma = sum(lista)
print('A soma dos números {} é {}'.format(lista, soma))

