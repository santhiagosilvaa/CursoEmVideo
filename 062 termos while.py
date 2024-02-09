#refaça o 061 e pergt se que mais termos ou parar



primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))

cont = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> ' .format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar? '))
print('Finalizado com {} termos. ' .format(total))