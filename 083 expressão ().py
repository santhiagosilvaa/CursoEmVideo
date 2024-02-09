#digita uma expressão que use parenteses; verificar se parenteses stão corretos

lista = []
abert = 0
fech = 0

exp = str(input('Digite a expressão: '))

for carac in exp:
    if carac == '(':
        lista.append('(')
    elif carac == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressão correta.')
else:
    print('Expressão errada')