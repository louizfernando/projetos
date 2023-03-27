from emoji import emojize
from random2 import randint, choice
print('Vamos jogar pedra, papel e tesoura.')
lista = ['pedra', 'papel', 'tesoura']
máquina = choice(lista)
#nmd == número da máquina
ndm = randint(0, 2)
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
#O JOGADOR GANHA
n = int(input('Qual você vai escolher? '))
while n != 0 and n != 1 and n != 2:
    print('JOGADA INVALIDA!')
    n = int(input('Qual você vai escolher? '))
if n == 0 and ndm == 1:
    print('VOCÊ GANHOU!')
elif n == 1 and ndm == 2:
    print('VOCÊ GANHOU!')
elif n == 2 and ndm == 0:
    print('VOCÊ GANHOU!')
#O JOGADOR EMPATA
elif n == ndm:
    print('EMPATE!')
#O JOGADOR PERDE

elif n == 0 and ndm == 2:
    print('VOCÊ PERDEU!')
elif n == 1 and ndm == 0:
    print('VOCÊ PERDEU!')
else:
    print('VOCÊ PERDEU!')
print(emojize(f'Eu escolhi {máquina} :smiling_face_with_sunglasses::smiling_face_with_sunglasses:'))
