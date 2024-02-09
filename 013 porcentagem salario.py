#leia o sálario e mostre novo salário com 15% de aumento

salario = float(input('Digite seu salário: '))
new_sal = salario * 1.15

print('Seu novo salário com aumento de 15% é R${:.2f} (real).' .format(new_sal))