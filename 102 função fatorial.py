#função fatorial(); dois valores -> primeiro fatoial;
# segundo show -> opcional; indica se será mostrado ou não na tela o prcesso

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(3, True))