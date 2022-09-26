import random
import emoji
import artes


def resultado(ganhou):
    """
    Função para exibir menjagem da mão do computador e resuldados de vitória, derrota ou empate.
    :param ganhou: inteiro 1 para ganhou, 2 para perdeu e 3 para empate.
    :return: String com mesagem correspondente a parametros e cartas nas mãos do computador e jogador
    """
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
    """
    Função que atualiza a soma das cartas do jogador e computador
    :return: Atualizção da soma das cartas
    """
    global pontuação_jogador, pontuação_computador
    pontuação_jogador = sum(jogador_mão)
    pontuação_computador = sum(computador_mão)


def resposta_jogador(msg=''):
    """
    Função de mensagem ao usuario, aguarda um input, retorna a resposta.
    :param msg: String, pergunta ao usuario.
    :return: reposta da mensagem
    """
    return input(str(msg)).strip().upper()


def separador():
    """
    Imprime um separador para melhor visualização do programa pelo usário.
    :return:
    """
    print(50 * '=')


def blackjack():
    """
    Função Recursiva, que roda o programa.
    :return:
    """
    global fim_de_jogo, turno_jogador, pontuação_jogador, pontuação_computador, computador_mão, jogador_mão
    pontuação_jogador = 0
    pontuação_computador = 0
    fim_de_jogo = False
    turno_jogador = True
    jogador_mão = [random.choice(cartas), random.choice(cartas)]  # Escolhe cartas iniciais ao jogador.
    computador_mão = [random.choice(cartas), random.choice(cartas)] # Escolhe cartas iniciais ao Computador.
    # Loop principal do jogo.
    while not fim_de_jogo:
        # Loop do turno do jogador
        while turno_jogador:
            # Mantem a soma das cartas atualizadas a cada loop.
            soma_pontuação()
            # Verifica o BlackJack inicial do computador.
            if computador_mão.count(11) == 1 and computador_mão.count(10) == 1 and sum(computador_mão) == 21:
                fim_de_jogo = True
                resultado(2)
                # Para loop do turno jo jogador
                break
            # Verificaca o Blackjack inicial do Jogador
            elif jogador_mão.count(11) == 1 and jogador_mão.count(10) == 1 and sum(jogador_mão) == 21:
                fim_de_jogo = True
                resultado(1)
                # Para turno do loop do jogador
                break
            # Verifica Ases na mão do jogador e caso seja maior que 21 os 11 viram 1
            if pontuação_jogador > 21:
                for i, v in enumerate(jogador_mão):
                    if v == 11:
                        jogador_mão[i] = 1
                        soma_pontuação()
            # Caso mesmo com Ases valendo 1 a soma passe de 21 o jogador perde
            if pontuação_jogador > 21:
                fim_de_jogo = True
                resultado(2)
                # Para turno do loop do jogador
                break
            # Mostra Cartar do jogador, soma e carta do computador
            print(f'Suas Cartas são {jogador_mão}, um total de {pontuação_jogador}')
            print(f'Primeira Carta do Computador {computador_mão[0]}')
            separador()
            # Define se o turno do jagador terina
            tirar_cartas = resposta_jogador('Você Deseja tirar mais uma carta?\nDigite (S) ou (N): ')
            separador()
            if tirar_cartas == 'S':
                # Indexa mais uma carta a mão do jogador
                jogador_mão.append(random.choice(cartas))
            elif tirar_cartas == 'N':
                # Para o loop do turno do jogador
                turno_jogador = False
        if fim_de_jogo:
            # Verifica se o fim de jogo é verdadeiro e para um loop principal.
            break
        # Inicia turno do computador
        while pontuação_computador < 17:
            # Indexa cartas a mão do computador
            computador_mão.append(random.choice(cartas))
            soma_pontuação()
        if pontuação_computador > 21:
            # Define vitoria
            resultado(1)
        elif pontuação_computador > pontuação_jogador:
            # Define Derrota
            resultado(2)
        elif pontuação_computador < pontuação_jogador:
            # Define Vitoria
            resultado(1)
        else:
            # Define empate
            resultado(3)
        fim_de_jogo = True
    # Aguarda resposta e chama função novamente
    continuar = resposta_jogador('Deseja jogar novamente\nDigite [S] ou [N]: ')
    separador()
    if continuar == 'S':
        blackjack()
    else:
        print('Até a proxima. Obrigado por jogar.')


# Cartas Disponiveis do jogo
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(artes.logo_blackjack)
separador()
# Aguarda reposta do jogador para inicia jogo
iniciar = resposta_jogador('Deseja jogar uma partida de Black Jack?\nDigite [S] ou [N]: ')
separador()
if iniciar == 'S':
    # Chamada inicial da função do programa.
    blackjack()
else:
    print('Até logo')
