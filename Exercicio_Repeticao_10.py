numero_primeiro = int(input ("Digite um número inteiro:"))
numero_segundo = int(input("Digite outro número inteiro:"))

if numero_primeiro <= numero_segundo:   
    for numero in range(numero_primeiro, numero_segundo+1):
        print (numero, end=" ")
else:
    for numero in range(numero_primeiro, numero_segundo+1):
        print (numero, end=" ")