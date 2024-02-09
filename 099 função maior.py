from time import sleep

def maior(*num):
    print('Analisando..')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
    print()
    if num:
        m = max(num)
        print(f'O maior numero é {m}')
    else:
        print("Nenhum número fornecido.")

maior(2, 1, 7, 4, 9)
maior(5, 6, 8)
maior(5)
maior()
