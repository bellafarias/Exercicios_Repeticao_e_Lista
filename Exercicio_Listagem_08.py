vetorIdade = []
vetorAltura = []

vetorIdadeInvert = []
vetorAlturaInvert = []

funcionarioIdade = 0
funcionarioAltura = 0

print("Adicionar Idade dos Funcionários")
for idade in range (0, 5):
    funcionarioIdade = funcionarioIdade +1
    print("Funcionários", funcionarioIdade)
    vetorIdade.append (input())
print ("lista de idades", vetorIdade)

for idade in range (0, 5):
    vetorIdadeInvert.append(vetorIdade.pop())
print("lista de idades (Ao contrário):", vetorIdadeInvert)

print("Adicionar Altura dos Funcionários")
for Altura in range (0, 5):
    funcionarioAltura = funcionarioAltura +1
    print("Funcionários", funcionarioAltura)
    vetorAltura.append (input())
print("Lista de Altura", vetorAltura)

for Altura in range (0, 5):
    vetorAlturaInvert.append(vetorAltura.pop())
print("lista de alturas (AO contrário):", vetorAlturaInvert)