from random import randint
from artes import logo_adivinhe_numero


def adivinha(n):
    print(f'Voce tem {tentativas} tentativas')
    global fim
    sugestao = int(input('Adivinhe o numero entre 1 e 100: '))
    if n == sugestao:
        print('Parabens, voce acertou o numero!')
        fim = True
    elif n > sugestao:
        print('Muito baixo.')
        return tentativas - 1
    elif n < sugestao:
        print('Muito alto.')
        return tentativas - 1


numero = randint(1, 100)
tentativas = 0
fim = False
print(logo_adivinhe_numero)
print("""
Bem vindo ao jogo de adivinhar números!
Advinhe um número entre 1 e 100""")
print(f'Shhh! A resposta é {numero}')
print('Em qual dificuldade deseja jogar?')
dificuldade = str(input('Digite Facil ou Dificil: '))
if dificuldade[0] in 'Ff':
    tentativas = 10
elif dificuldade[0] in 'Dd':
    tentativas = 5

while not fim:
    if tentativas > 0:
        print('Tente novamente')
        tentativas = adivinha(numero)
    elif tentativas == 0:
        print('Suas Tentativas acabaram')
        fim = True
print('Fim de jogo')
