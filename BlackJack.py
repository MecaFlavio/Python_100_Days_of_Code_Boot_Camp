import random
import emoji
import artes


def resultado(ganhou):
    print(f'Sua mão tem {jogador_mão} e o computador tem {computador_mão}.')
    if ganhou == 1:
        print(f"Você tem {pontuação_jogador} e o Computador tem {pontuação_computador}. Você Ganhou!",
              emoji.emojize(':smile:', language='alias'))
    elif ganhou == 2:
        print(f"Você tem {pontuação_jogador} e o Computador tem {pontuação_computador}. Você Perdeu!",
              emoji.emojize(':weary:', language='alias'))
    else:
        print(f"Você tem {pontuação_jogador} e o Computador tem {pontuação_computador}. Empate!",
              emoji.emojize(':expressionless:', language='alias'))
    separador()


def soma_pontuação():
    global pontuação_jogador, pontuação_computador
    pontuação_jogador = sum(jogador_mão)
    pontuação_computador = sum(computador_mão)


def resposta_jogador(msg=''):
    return input(str(msg)).strip().upper()


def separador():
    print(50 * '=')


def blackjack():
    global fim_de_jogo, turno_jogador, pontuação_jogador, pontuação_computador, computador_mão, jogador_mão
    pontuação_jogador = 0
    pontuação_computador = 0
    fim_de_jogo = False
    turno_jogador = True
    jogador_mão = [random.choice(cartas), random.choice(cartas)]
    computador_mão = [random.choice(cartas), random.choice(cartas)]
    while not fim_de_jogo:
        while turno_jogador:
            soma_pontuação()
            if computador_mão.count(11) == 1 and computador_mão.count(10) == 1 and sum(computador_mão) == 21:
                fim_de_jogo = True
                resultado(2)
                break
            elif jogador_mão.count(11) == 1 and jogador_mão.count(10) == 1 and sum(jogador_mão) == 21:
                fim_de_jogo = True
                resultado(1)
                break
            if pontuação_jogador > 21:
                for i, v in enumerate(jogador_mão):
                    if v == 11:
                        jogador_mão[i] = 1
                        soma_pontuação()
            if pontuação_jogador > 21:
                fim_de_jogo = True
                resultado(2)
                break
            print(f'Suas Cartas são {jogador_mão}, um total de {pontuação_jogador}')
            print(f'Primeira Carta do Computador {computador_mão[0]}')
            separador()
            tirar_cartas = resposta_jogador('Você Deseja tirar mais uma carta?\nDigite (S) ou (N): ')
            separador()
            if tirar_cartas == 'S':
                jogador_mão.append(random.choice(cartas))
            elif tirar_cartas == 'N':
                turno_jogador = False
        if fim_de_jogo:
            break
        while pontuação_computador < 17:
            computador_mão.append(random.choice(cartas))
            soma_pontuação()
        if pontuação_computador > 21:
            resultado(1)
        elif pontuação_computador > pontuação_jogador:
            resultado(2)
        elif pontuação_computador < pontuação_jogador:
            resultado(1)
        else:
            resultado(3)
        fim_de_jogo = True
    continuar = resposta_jogador('Deseja jogar novamente\nDigite [S] ou [N]: ')
    separador()
    if continuar == 'S':
        blackjack()
    else:
        print('Até a proxima. Obrigado por jogar.')


cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(artes.logo_blackjack)
separador()
iniciar = resposta_jogador('Deseja jogar uma partida de Black Jack?\nDigite [S] ou [N]: ')
separador()
if iniciar == 'S':
    blackjack()
else:
    print('Até logo')
