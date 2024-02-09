#digite um numero e mostre sua tabuada

#função tabuada
def tabuada(n):
    for i in range(1,11): # i vai de 1 a 10
        r = i * n # calculos
        print('{} x {:2} = {}' .format(n, i, r)) #print na tela

n = int(input(('Digite um numero: '))) #pede ao user para digitar
print('=' * 15)
tabuada(n) #chama a função
print('=' * 15)