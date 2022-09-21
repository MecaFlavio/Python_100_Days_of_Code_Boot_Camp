# Calculadora
from artes import logo_calculadora


def soma(n1, n2):
    return n1 + n2


def subtr(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def divi(n1, n2):
    return n1 / n2


def calculadora():  # Função recursiva
    continuar = True
    num_1 = float(input('Qual o primeiro número? '))
    while continuar:
        for k in operações:
            print(k)
        sinal_operação = input('Escolha uma operação da lista acima: ')
        num_2 = float(input('Qual o proximo número? '))
        função_calculo = operações[sinal_operação]
        resposta = função_calculo(num_1, num_2)
        print(f"{num_1} {sinal_operação} {num_2} = {resposta}")
        if input(f'Digite (S) para continuar, (N) para novo calculo: ').strip().upper() == 'S':
            num_1 = resposta
        else:
            continuar = False
            calculadora()  # Chama a função novamente


operações = {'+': soma,
             '-': subtr,
             '*': multi,
             '/': divi
             }

print(logo_calculadora)
calculadora()
