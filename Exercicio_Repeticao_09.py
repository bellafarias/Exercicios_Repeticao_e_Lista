numeros_1_a_50 = list(range(1,51))
numeros_impares = []
print("Números inteiros:", numeros_1_a_50)

for impares in numeros_1_a_50:
    if impares % 2 != 0: 
        numeros_impares.append(impares)
print ("números impares:", numeros_impares)