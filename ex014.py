#tabuada v.2.0
#fazer uma tabuada usando laço for

num = int(input('Digite o número da tabuada desejada: '))
lista = []
for i in range(11):
    resultado = num * i
    lista.append(resultado)
print(lista)
