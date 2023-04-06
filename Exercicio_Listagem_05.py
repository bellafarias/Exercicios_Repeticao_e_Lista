numbers = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20]
numbersPares = []
numbersImpares = []
print('lista de números:', numbers)

for valor in numbers:
    if valor%2 == 0: 
        numbersPares.append(valor)
    else:
        numbersImpares.append(valor)

print('Números pares:',numbersPares)
print('Números impares:',numbersImpares)