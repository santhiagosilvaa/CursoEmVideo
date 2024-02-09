#criar menu
import dados
from time import sleep
import arquivo

arq = 'cursoemvideo.txt'

if not dados.arquivoExiste(arq):
    dados.criarArquivo(arq)

while True:
    resposta = dados.menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        dados.lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        dados.cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        dados.cadastrar(arq, nome, idade)
        sleep(1)
    elif resposta == 3:
        dados.cabeçalho('SAINDO DO SISTEMA')
        sleep(1)
        break
    else:
        print('ERRO! Digite um opçao valida')
        sleep(1)