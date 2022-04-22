#Maior ou menor da sequência
#input peso de 5 pessoas
# maior e o menor peso lidos

lista = []

for i in range(0,6):
    peso = float(input('Digite o peso: '))
    lista.append(peso)
print('\n')
print('Pesos digitados', lista)
print('\n')

maior = lista[0]

if lista[1] > maior:
    maior = lista[1]
if lista[2] > maior:
    maior = lista[2]
if lista[3] > maior:
    maior = lista[3]
if lista[4] > maior:
    maior = lista[4]

menor = lista[0]

if lista[1] < menor:
    menor = lista[1]
if lista[2] < menor:
    menor = lista[2]
if lista[3] < menor:
    menor = lista[3]
if lista[4] < menor:
    menor = lista[4]

print('Maior: {:.20}Kg'.format(maior))
print('Menor: {:.20}Kg'.format(menor))
