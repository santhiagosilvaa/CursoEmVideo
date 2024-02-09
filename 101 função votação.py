#função voto(); recebe ano de nasc; mostre voto negado, opcional ou obrigatorio


def voto(nasc):
    from datetime import date

    idade = date.today().year - nasc

    if idade < 16:
        return f'Com {idade} anos: VOTO PROIBIDO'
    elif 16 <= idade <= 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO'


nasc = int(input('Digite sua data de nasc: '))
print(voto(nasc))