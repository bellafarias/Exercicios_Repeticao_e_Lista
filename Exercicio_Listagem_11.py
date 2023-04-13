cores_massas = ['azul', 'roxo', 'amarelo', 'violeta', 'rosa','laranja', 'verde', 'vermelho', 'cinza', 'ciano']
letrinhas_massas = ['A','I','L','M','F','N','G','H','J','S']
cidades_massas = ['Curitiba','São Paulo','Minas Gerais','Rio de Janeiro','Fortaleza','Goias','Paraty','Higienopólis','Ubatuba','Uberlândia']
lista_Vazia = []

for elementos in range(10):
    lista_Vazia.append (cores_massas[elementos])
    lista_Vazia.append (letrinhas_massas[elementos])
    lista_Vazia.append (cidades_massas[elementos])

print ("Cores Legais:", cores_massas)
print ("Letrinhas Legais:",letrinhas_massas)
print ("Ciadades fofas:", cidades_massas)
print ('Lista Intercalada:', lista_Vazia)
