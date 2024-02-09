#refaça ex 009, tabuada q user escolher


n = int(input('Digite um número que deseja usar na tabuada: '))
result = 0
print('=*' * 10)
print('Tabuada do {}' .format(n))
print('=*'*10)

for tab in range(1,11):
    print('{:2} X {} = {}' .format(tab, n, tab * n))

print('=*' * 10)