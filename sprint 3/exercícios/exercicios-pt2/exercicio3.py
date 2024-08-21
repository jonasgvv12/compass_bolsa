palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range (len(palavras)):
    palindromo = palavras[i]
    if list(reversed(palindromo)) == list(palindromo):
        print(f"A palavra: {palindromo} é um palíndromo")
    else:
        print(f"A palavra: {palindromo} não é um palíndromo")