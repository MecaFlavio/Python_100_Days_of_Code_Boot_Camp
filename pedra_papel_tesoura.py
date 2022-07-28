import random

pedra = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
papel = '''           
                   _
               _  / |
              / \ | | /\
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
                |     |

'''
tesoura = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
mão = [pedra, papel, tesoura]

print('Bem Vindo ao pedra papel e tesoura!\n'
      'Escloha:\n'
      '1 - PEDRA\n'
      '2 - PAPEL\n'
      '3 - TESOURA')
jogador = int(input('Digite o numero de sua escolha:\n'))
computador = random.randint(1, 3)
print('Sua escloha:')
print(mão[jogador - 1])
print('Escolha do Computador:')
print(mão[computador - 1])
if jogador == 3 and computador == 2:
    print('Voce Ganhou!')
elif jogador == 2 and computador == 1:
    print('Voce Ganhou!')
elif jogador == 1 and computador == 3:
    print('Voce Ganhou!')
elif jogador == computador:
    print('Houve um empate!')
else:
    print('Voce Perdeu!')
