def metade(valor, formato=False):
    metade = valor / 2
    return metade if formato is False else moeda(metade)
def dobro(valor, formato=False):
    dobro = valor * 2
    return dobro if formato is False else moeda(dobro)
def aumentar(valor, a, formato=False):
    aumentar = valor + (valor * (a/100))
    return aumentar if formato is False else moeda(aumentar)
def diminuir(valor, d, formato=False):
    diminuir = valor - (valor * (d/100))
    return diminuir if formato is False else moeda(diminuir)

def moeda(valor, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumomoeda(valor, a=10, d=10):
    print('-'*30)
    print('RESUMO DO VALOR' .center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{a}% de aumento: \t{aumentar(valor, a, True)}')
    print(f'{d}% de redução: \t{diminuir(valor, d, True)}')
    print('-' * 30)

def leiaDinheiro(msg):
     valido = False
     while not valido:
         entrada = str(input(msg)).replace(',','.').strip()
         if entrada.isalpha() or entrada == '':
             print('ERRO! Digite um numero válido.')
         else:
             valido = True
     return float(entrada)

def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('Você não digitou um numero inteiro. Digite novamente: ')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu não digitar.')
            return 0
        else:
            return i

def leiaReal(msg):
    while not False:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('Você não digitou um numero real. Digite novamente: ')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu não digitar.')
            return 0
        else:
            return real

