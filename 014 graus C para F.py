#Digite a temperatura em ºC e converta para ºF

grausC = float(input('Digite a temperatura em ºC: '))

grausF = (9/5 * grausC) + 32

print('A temperatura em ºC é {:.1f}º e em ºF é {:.1f}º' .format(grausC, grausF))