Validade_nome = False
while Validade_nome == False:
    nomeinicial = (input("Digite seu nome:"))
    if len(nomeinicial) > 3:
        Validade_nome=True
    else :
        print ("Tente novamente, digite um nome com mais de 3 carcteres")

Validade_idade = False
while Validade_idade == False:
    idadeVetor = float(input("Digite sua Idade:"))
    if idadeVetor > 0 and idadeVetor < 150:
        Validade_idade = True
    else :
        print ("Tente novamente, digite uma idade que seja maior que 0 e menor que 150")

Validade_salario = False
while Validade_salario== False:
    SalarioVetor = float(input("Digite seu salário(sem ponto e virgula):"))
    if SalarioVetor > 0:
        Validade_salario= True
    else :
        print ("Tente novamente, digite um salário que seja maior que 0.")

validade_sexo = False
sexo = [ "F", "M", "I", "f", "m", "i"]
while validade_sexo== False:
    sexoVetor= (input("Digite seu Gênero, F para feminino, M para Masculino e I para Indefinido:"))
    if sexoVetor in sexo:
        validade_sexo= True
    else :
        print ("Tente novamente, digite uma dessas opções, F para feminino, M para Masculino e I para Indefinido.")

validade_EstadoCivil = False
estado= [ "S", "D", "V", "C", "c", "v", "d", "s"]
while validade_EstadoCivil== False:
    vetorEstado= (input("Digite seu Estado Civil, S para Solteiro, D para Divorciado, V para Viúvo, C para Casado:"))
    if vetorEstado in estado:
        validade_EstadoCivil= True
    else :
        print ("Tente novamente, digite uma dessas opções, S para Solteiro, D para Divorciado, V para Viúvo, C para Casado.")
print("Obrigado pela resposta!")