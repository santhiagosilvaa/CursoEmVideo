# leia algo - fale seu tipo (int, float, str, bool) - e todas informações possíveis

n1 = input('Digite algo: ')
print(n1)
print(type(n1))

print('É alfanumérico? ', n1.isalnum())
print('É alfabético? ', n1.isalpha())
print('É número? ', n1.isnumeric())
print('É maiusculo? ', n1.isupper())
print('É ASCII? ', n1.isascii())
print('É decimal? ', n1.isdecimal())
print('É um digito? ', n1.isdigit())
print('É identificador? ', n1.isidentifier())
print('É minusculo? ', n1.islower())
print('É printtable? ', n1.isprintable())
print('É espaço? ', n1.isspace())
print('É capitalizada? ', n1.istitle())

n2 = int(input('Digite algo2: '))
print(n2)
print(type(n2))

n3 = bool(input('Digite algo3: '))
print(n3)
print(type(n3))

n4 = float(input('Digite algo4: '))
print(n4)
print(type(n4))



