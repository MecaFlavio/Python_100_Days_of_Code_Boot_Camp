from os import system
import artes

# Variaveis
nome = str
oferta = float
dicionario_de_ofertas = {}
continuar = True


def maior_oferta(ofertantes):
    print(artes.logo_leilão)
    maior = 0
    ganhador = str
    for k, v in ofertantes.items():
        if v > maior:
            ganhador = k
            maior = v
    print(f'O Ganhador é {ganhador} com a oferta de {maior}')


while continuar:
    print(artes.logo_leilão)
    print("Bem vindo ao Programa de Leilão Secreto")
    nome = str(input('Qual o seu nome?\n'))
    oferta = float(input('Qual o valor da Oferta?\n'))
    dicionario_de_ofertas[nome] = oferta
    system('cls')
    print(artes.logo_leilão)
    pergunta = str(input('Ha outra pessoa para ofertar?\n')).strip().lower()
    if pergunta == 'sim':
        system('cls')
    else:
        system("cls")
        continuar = False

maior_oferta(dicionario_de_ofertas)
