#função notas(); usar dicionario ->
#quantidade de notas; maior nota; média da turma; situação (opcional)

def notas(*n, sit=False):
    boletinho = {}
    boletinho['total'] = len(n)
    boletinho['maior'] = max(n)
    boletinho['menor'] = min(n)
    boletinho['media'] = sum(n) / len(n)

    if sit == True:
        if boletinho['media'] >= 7:
            boletinho['sit'] = 'Aprovado'
        elif boletinho['media'] >= 5:
            boletinho['sit'] = 'Recuperação'
        else:
            boletinho['sit']= 'Reprovado'

    return boletinho

resp = notas(5, 6, 8, 0, sit=True)
print(resp)