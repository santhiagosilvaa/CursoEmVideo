#aprovar emprestimo para compra de uma casa
#pergt: valor da casa; salario; quantos anos
#calcule prestação - não pode exceder 30% do salario ou será negado

valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário: '))
prazo = int(input('Em quantos anos pagará o empréstimo:'))

parcela = valor / (prazo * 12)

print('O valor da parcela é de R${:.2f}' .format(parcela))

if parcela > (sal * 30/100):
    print('A parcela de R${:.2f}, excede 30% do salário. \n\033[41mEMPRÉSTIMO NEGAGO\033[m' .format(parcela))

else:
    print('\n\033[42mEMPRÉSTIMO APROVADO\033[m' .format(parcela))
