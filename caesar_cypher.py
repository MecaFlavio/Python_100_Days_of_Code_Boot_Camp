from artes import logo_caesar_cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
            ]
continuar = True


def encrypt(escolha, mensagem, intervalo):
    alphabet2 = alphabet[0:intervalo]
    alphabet3 = alphabet[intervalo:] + alphabet2
    cripto = ''
    for letra in mensagem:
        if letra not in alphabet:
            cripto += str(letra)
        else:
            if escolha == 'codigo':
                cripto += alphabet3[alphabet.index(letra)]
            elif escolha == 'decifrar':
                cripto += alphabet[alphabet3.index(letra)]
    print(f"O codigo decifrado é {cripto}")


print(logo_caesar_cypher)

while continuar:
    direction = input("Digite 'Codigo' para Criptografar, digite 'Decifrar' para Descriptografar:\n").lower().strip()
    text = input("Digite sua mensagem:\n").lower().strip()
    shift = int(input("Digide um numero para o intervalo:\n"))
    shift = shift % 26

    encrypt(escolha=direction, mensagem=text, intervalo=shift)
    pergunta = str(input('Digite "sim" se desaja continuar, ou "não" para encerrar?:\n')).lower().strip()
    if pergunta == 'não' or pergunta == 'nao':
        continuar = False
        print('Até logo!')
