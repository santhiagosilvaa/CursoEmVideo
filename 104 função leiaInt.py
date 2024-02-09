#função leiaInt(); aceitar apenas numeros inteiros

def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('Erro! Digite um numero válido')
    return valor

n = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {n}')
