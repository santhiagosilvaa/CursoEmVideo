#leia nome e duas notas -> lista composta;
# mostre as notas e média e permita mostrar as notas individualmente

completa = []
aluno = []
media = []
media1 = cont = 0

while True:
    nome = str(input('Digite o nome: '))
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    aluno.append(nota2)

    media1 = (nota1+nota2) / 2
    media.append(media1)

    completa.append(aluno[:])
    aluno.clear()

    cont += 1

    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if op == 'N':
        break

print(f'{"Nº":<2} {"NOME":<10} {"MÉDIA":<4}')
print('-'*30)
for l in range(0, cont):
    print(f'{l+1:<2} {completa[l][0]:<10} {media[l]:<4} \n')
print('-' * 30)

while True:
    x = str(input('Deseja consultar um aluno individualmente? [S/N]: ')).upper().strip()[0]
    if x == 'N':
        break
    else:
        op = int(input('Digite a numeração desejada: '))

    for l in range(op-1, op):
        print(f'{op} - Aluno: {completa[op-1][0]}. \nNotas: {completa[op-1][1]} - {completa[op-1][2]} \nMédia: {media[op-1]} \n')
