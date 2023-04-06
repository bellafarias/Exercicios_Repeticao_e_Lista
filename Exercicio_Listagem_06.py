Notinhas = [['Leticia', [10, 9, 8, 9]] , ['Maykon', [7, 9, 5, 1]] , ['Mayara', [6, 6, 8, 10]] , ['Gabriela', [7, 8, 7, 4]] , ['Laura', [7, 6, 3, 2]] , ['Natália', [2, 7, 9, 9]] , ['Cintia', [3, 8, 9, 10]] , ['Lorena', [3, 9, 6, 2]] , ['Eduardo', [2, 1, 5, 3]] , ['Henrique', [1, 5, 9, 4]]]

for estudante in Notinhas:
    notas = estudante[1]
    media = sum(notas) / len(notas)
    print(f"A média das notas de {estudante[0]} é {media:.2f}")