#Progressão Aritmétrica
#input primeiro termo e a razao de uma PA
#no final mostrar od 10 primeiros termos da progressao

print('-=' * 12)
print('Progressão Aritmétrica')
print('-=' * 12)

primeiro_termo = float(input('Primeiro termo: '))
razao = float(input('Razão da PA: '))

print('-=' * 12)

lista = []
for n in range(10):
    termo = primeiro_termo + ((n - 1)*razao)
    lista.append(termo)

print('Os 10 primeiros termos da PA é:\n'
      ,lista)

