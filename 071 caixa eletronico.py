#simule caixa eletronico; pergt valor inteiro; e diga quantas cédulas
#50; 20; 10; 1

valor = int(input('Digite o valor a ser sacado: R$'))

n1 = (valor // 50)
n2 = (valor - n1*50) // 20
n3 = (valor - n1*50 - n2*20) // 10
n4 = (valor - n1*50 - n2*20 - n3*10)

if n1 > 0:
    print(f'Total de {n1} cédulas de R${50}')

if n2 > 0:
    print(f'Total de {n2} cédulas de R${20}')

if n3 > 0:
    print(f'Total de {n3} cédulas de R${10}')

if n4 > 0:
    print(f'Total de {n4} cédulas de R${1}')

