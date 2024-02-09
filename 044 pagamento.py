#calcule o valor a ser pago
#a vista dinheiro/cheque 10% desconto ; a vista cartão 5% descont; 2x preço normal; 3x ou + 20% juros

valor = float(input('Qual o valor do produto? '))
cond = int(input('Escolha a forma de pagamento. \n1 - dinheiro/cheque. \n2 - à vista cartão. \n3 - 2x cartão. \n4 - 3x+ cartão. \nOpção: '))

if cond == 1:
    vf = valor * 0.9
    print('Valor original: R${:.2f}. \nValor no dinheiro/cheque: R${:.2f}' .format(valor, vf))

elif cond == 2:
    vf = valor * 0.95
    print('Valor original: R${:.2f}. \nValor à vista no cartão: R${:.2f}'.format(valor, vf))

elif cond == 3:
    vf = valor
    print('Valor original: R${:.2f}. \nValor em 2x no cartão: R${:.2f}'.format(valor, vf))

elif cond == 4:
    vf = valor * 1.2
    print('Valor original: R${:.2f}. \nValor em 3x ou mais no cartão: R${:.2f}'.format(valor, vf))
