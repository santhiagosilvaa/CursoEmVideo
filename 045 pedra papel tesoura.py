#crie um jogo para jogar jokenpô

from random import choice
import emoji

op = int(input('Faça sua escolha: \n1 - Pedra \n2 - Papel \n3 - Tesoura \nEu escolho a op: '))

joken = ['Pedra', 'Papel', 'Tesoura']
pc = choice(joken)

if pc == 'Pedra':
    if op == 1:
        print('O PC escolheu {} e você também. Deu empate.' .format(pc))
        print(emoji.emojize(':oncoming_fist_medium-dark_skin_tone:'), '-',
              emoji.emojize(':oncoming_fist_medium-dark_skin_tone:'), '->', 'EMPATE')

    elif op == 2:
        print('O PC escolheu {} e vocẽ Papel. Você ganhou. ' .format(pc))
        print(emoji.emojize(':oncoming_fist_medium-dark_skin_tone:'), '-',
              emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:'), '->', 'VOCÊ GANHOU')

    elif op == 3:
        print('O PC escolheu {} e vocẽ Tesoura. Você perdeu. ' .format(pc))
        print(emoji.emojize(':oncoming_fist_medium-dark_skin_tone:'), '-',
              emoji.emojize(':victory_hand_medium-dark_skin_tone:'), '->', 'VOCÊ PERDEU')

elif pc == 'Papel':
    if op == 1:
        print('O PC escolheu {} e você Pedra. Você perdeu.'.format(pc))
        print(emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:'), '-',
              emoji.emojize(':oncoming_fist_medium-dark_skin_tone:'), '->', 'VOCÊ PERDEU')

    elif op == 2:
        print('O PC escolheu {} e vocẽ também. Deu empate '.format(pc))
        print(emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:'), '-',
              emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:'), '->', 'EMPATE')

    elif op == 3:
        print('O PC escolheu {} e vocẽ Tesoura. Você ganhou. '.format(pc))
        print(emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:'), '-',
              emoji.emojize(':victory_hand_medium-dark_skin_tone:'), '->', 'VOCÊ GANHOU')

elif pc == 'Tesoura':
    if op == 1:
        print('O PC escolheu {} e você Pedra. Você ganhou.'.format(pc))
        print(emoji.emojize(':victory_hand_medium-dark_skin_tone:'), '-',
              emoji.emojize(':oncoming_fist_medium-dark_skin_tone:'), '->', 'VOCÊ GANHOU')

    elif op == 2:
        print('O PC escolheu {} e vocẽ Papel. Você perdeu. '.format(pc))
        print(emoji.emojize(':victory_hand_medium-dark_skin_tone:'), '-',
              emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:'), '->', 'VOCÊ PERDEU')

    elif op == 3:
        print('O PC escolheu {} e vocẽ Tesoura. Deu empate. '.format(pc))
        print(emoji.emojize(':victory_hand_medium-dark_skin_tone:'), '-',
              emoji.emojize(':victory_hand_medium-dark_skin_tone:'), '->', 'EMPATE')



'''print(emoji.emojize(':oncoming_fist_medium-dark_skin_tone:')) #pedra
print(emoji.emojize(':hand_with_fingers_splayed_medium-dark_skin_tone:')) #papel
print(emoji.emojize(':victory_hand_medium-dark_skin_tone:')) #tesoura'''