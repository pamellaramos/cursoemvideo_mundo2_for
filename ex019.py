#Grupo da maioridade
# input ano de nascimento de 7 pessoas
# mostre quem atingiu, ianda não ou já passou da maioridade (21 anos)
import datetime

for i in range(1,8):
    ano = int(input('Digite seu ano de Nascimento: '))

    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    ano_atual = date.year

    calculo = ano_atual - ano
    print('Ano de Nacimento: {}'.format(ano))
    if calculo == 21:
        print('Atingiu a maioridade')
    elif calculo < 21:
        print('Ainda não atingiu a maioridade')
    else:
        print('Já passou da maioridade')

