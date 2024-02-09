#leia um ano mostre se ele é bissexto

from datetime import date # import para datas

ano = int(input('Digite um ano ou digite 0 para ano atual: '))

if ano == 0:
    ano = date.today().year #seleciona o ano atual

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto' .format(ano))

else:
    print('O ano {} NÃO é bissexto' .format(ano))