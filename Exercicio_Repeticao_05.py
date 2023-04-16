while True:
    PovoA = False 
    while PovoA == False:
        populosoVetorA = float(input("Insira um número para a população do país A (sendo maior que 0):"))
        if populosoVetorA > 0:
            print ("Obrigado!")
            PovoA = True 
        else:
            print("Por Favor, tente novamente, Insira um número que seja maior que 0:")

    Taxa_Pais_A = False 
    while Taxa_Pais_A == False:
        Taxa_Vetor_A = float(input("Insira um número para a Taxa anual(em decimal) do país A (sendo maior que 0):"))
        if Taxa_Vetor_A >= 0:
            print ("Obrigado!")
            Taxa_Pais_A = True 
        else:
            print("Por Favor, tente novamente, Insira um número que seja maior que 0):")

    PovoB = False 
    while PovoB == False:
        populosoVetorB = float(input("Insira um número para a população do país B (sendo maior que 0):"))
        if populosoVetorB > 0:
            print ("Obrigado!")
            PovoB = True 
        else:
            print("Por Favor, tente novamente, Insira um número que seja maior que 0):")

    Taxa_Pais_B = False 
    while Taxa_Pais_B == False:
        Taxa_Vetor_B = float(input("Insira um número para a Taxa anual(em decimal) do país B (sendo maior que 0):"))
        if Taxa_Vetor_B > 0:
            print ("Obrigado!")
            Taxa_Pais_B = True 
        else:
            print("Por Favor, tente novamente, Insira um número que seja maior que 0):")

    anos = 0

    while  populosoVetorA < populosoVetorB:
        anos = anos +1
        populosoVetorA = populosoVetorA * ( Taxa_Vetor_A +1)
        populosoVetorB = populosoVetorB * ( Taxa_Vetor_B +1)
    print("Serão necessários",anos, "anos para que a população a Ultrapasse a população B")

    finalzinho = input("Gostaria de oferecer outro valor para a simulação?, digite s para sim e n para não:")
    if finalzinho.lower() == "n":
            break