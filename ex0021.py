#Analisador completo
#input nome, idade, sexo de 4 pessoas
#mostrar a média de idades do grupo, nome do homem mais velhor e quantas mulheres tem menos de 25 anos.

import numpy as np
somaidade = 0
media = 0
maiorhomem = 0
nomevelho = 0
totmulher = 0

for i in range(4):
    nome = input('Nome: ').upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_sexo.append(sexo)

    if n == 1 and sexo == 'M':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maiorhomem:
        maiorhomem = ifsfr
        nomevelho = nome
    if sexo in 'F' and idade <20:
        totmulher = totmulher + 1

media = soma
print('A média é {}anos'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(maiorhomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))