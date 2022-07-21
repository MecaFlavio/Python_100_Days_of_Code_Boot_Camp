print('''
                                                 .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')
print('Bem vindo à Ilha do Tesouro!\n'
      'Seu objetivo é achar o tesouro!')
resposta = str(input('Vamos começar? Digite S ou N:\n')).upper().strip()
if resposta == 'S':
    print('Você está dentro de uma ruina de um antigo templo.\n'
          'Há duas portas na sala uma a Esquerda e outra a Direita.')
    resposta = str(input('Em qual deseja entrar? E ou D:\n')).upper().strip()
    if resposta == 'E':
        print('Você entrou numa sala cheia de espinhos no teto e foi esmagado! GAME OVER')
    elif resposta == 'D':
        print('Agora voce está em um corredor com duas direções e tem um bloco solto na chão. ')
        resposta = str(input('Deseja ir seguir a Esquerda, a Direita ou Pisar no bloco?\n'
                             'E, D ou P:\n')).upper().strip()
        if resposta == 'D':
            print('Você caiu em um buraco ao passar pelo corredor e esta morto. GAME OVER!')
        elif resposta == 'E':
            print('Uma lamina cortou sua cabeça ao passar pelo corredor! GAME OVER!')
        elif resposta == 'P':
            print('Uma porta secreta se abriu.')
            resposta = str(input('Deseja entrar? S ou N:\n')).upper().strip()
            if resposta == 'N':
                print('O corredor desmorona. GAME OVER!')
            elif resposta == 'S':
                print('Você esta em uma sala com dois baus.')
                resposta = int(input('Qual deseja abrir? 1 ou 2:\n'))
                if resposta == 1:
                    print('Dentro do Baú ha um ninho de viboras. GAME OVER!')
                elif resposta == 2:
                    print('Voce achou o tesouro! VOCÊ VENCEU!!!!')
                    print('''
                    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
                    ''')
elif resposta == 'N':
    print('Vemos que não é merecedor! GAME OVER.')
