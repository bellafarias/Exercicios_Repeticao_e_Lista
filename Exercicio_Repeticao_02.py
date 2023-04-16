Senha_certa= False

while Senha_certa == False:
    print("Digite um Usuário massa:")
    usuario_entrada = input()
    print("Agora adicione uma senha (Diferente do nome de usuário):")
    senha_legal = input()
    if usuario_entrada != senha_legal:
        print("Perfeito meu mano!")
        Senha_certa =True
    else :
        print ("Tenta de novo colega")