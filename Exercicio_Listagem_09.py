VetorA = [17, 22, 13, 42, 24, 16, 27, 82, 9, 10]
NumerosQuadrados = []

for QuadradoNumero in VetorA:
    Quadrado = QuadradoNumero ** 2
    NumerosQuadrados.append(Quadrado)

soma = sum(NumerosQuadrados)

print("Números Padrões:", VetorA)
print("Números ao Quadrado:", NumerosQuadrados)
print("Soma dos Números ao quadrado:", soma)
    