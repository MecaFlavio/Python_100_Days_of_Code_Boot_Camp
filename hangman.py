# 'import.' das libs e modulos utilizados
import random
import hangman_logo_palavras

# Variaveis e listas
vidas = 6
palavra_ecolhida = []
fim_de_jogo = False

# Escolha da palavra através de lista em módulo criado
palavra = random.choice(hangman_logo_palavras.lista_palavras)  # utilização de módulo
for i in range(len(palavra)):
    palavra_ecolhida.append('_')

# print(f'Dica da palavra {palavra}')

# Inicio do loop
print(hangman_logo_palavras.logo)  # utilização de módulo
while not fim_de_jogo:

    # laço para criação de ‘interface’
    for i in range(len(palavra_ecolhida)):
        print(palavra_ecolhida[i], end=' ')
    print(hangman_logo_palavras.fases[vidas])  # utilização de módulo
    print(f'Adivinhe a palavra. Voce tem {vidas} chance(s).')
    escolha = str(input('Escolha uma letra: ')).lower()

    # laço para verificar se a letra corresponde a letras da palavra
    for posição in range(len(palavra)):
        letra = palavra[posição]
        if escolha == letra:
            palavra_ecolhida[posição] = letra

    # Condições para verificar acerto ou erro do usuario e definir fim do jogo
    if escolha not in palavra:
        print(f'A letra {escolha} não faz parte da palavra, voce perdeu uma chance.')
        vidas -= 1
        if vidas == 0:
            fim_de_jogo = True
            print('Suas Chances acabaram. Voce perdeu.')
            print(hangman_logo_palavras.fases[vidas])  # utilização de módulo
    if '_' not in palavra_ecolhida:
        print(f'A palavra é {palavra}')
        print('Você Ganhou')
        fim_de_jogo = True
