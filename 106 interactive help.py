#função que usa interactive help

def interactivehelp():
    while True:
        n = str(input('Função ou Biblioteca (escreva FIM para finalizar): '))
        if n.upper().strip() == 'FIM':
            break
        help(n)

interactivehelp()
