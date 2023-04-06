palavrafofa = ['t','e','c','n','o','l','o','g','i','a']
consonants = 0

for letras in palavrafofa:
    if letras not in 'aeiou':
        consonants=consonants + 1
        print('consoantes:', letras)

print('Número de consoantes:',consonants)