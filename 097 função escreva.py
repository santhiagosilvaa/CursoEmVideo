#função escreva(); recebe um texto

def escreva(frase):
    tam = len(frase) + 4
    print('-' * tam)
    print(f'  {frase}')
    print('-' * tam)


frase = str(input('Digite uma frase: '))
escreva(frase)