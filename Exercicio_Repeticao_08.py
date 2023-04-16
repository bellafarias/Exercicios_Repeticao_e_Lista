numeros_descolados = [100, 200, 300, 400, 500]
print("Lista de Números:", numeros_descolados)

numeros_gerais = []
for numeros in numeros_descolados:
    numeros_gerais.append(numeros)
soma = sum (numeros_gerais)
print("Soma dos Números:", soma)
media = sum(numeros_gerais)/ len(numeros_gerais)
print("A média dos Números é:", media)