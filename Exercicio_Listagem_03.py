NotasAlunos = [70, 80, 90, 100]
print ('Notas dos Alunos', NotasAlunos)

quantidade = len(NotasAlunos)
soma = 0 

for valores in NotasAlunos:
    soma = soma + valores

print('Média das notas dos alunos', soma/quantidade)

