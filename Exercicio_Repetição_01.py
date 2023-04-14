Nota_valida = False

while not nota_valida:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, por favor, digite uma nota entre 0 e 10:")
    else:
        nota_valida = True
        print("Obrigado(a)!")