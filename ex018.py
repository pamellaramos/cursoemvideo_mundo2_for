#Detector de Palíndromo
#input uma frase
#diga se é palíndromo

texto = input('Digite o seu texto: ').upper()
if str(texto) == str(texto)[::-1] :
    print("Palindrome")
else:
    print("Não é um Palindrome")