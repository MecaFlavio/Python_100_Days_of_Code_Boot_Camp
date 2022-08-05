# Projeto de Gerador de Senhas
import random

# Listas de Caracteres usaveis
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Variaveis e Listas
caracteres = []
caracteres_ordem = []
senha = ''

# Cabeçalho e 'inputs'
print('Seja Bem vindo(a) ao gerador de senhas.')
num_letras = int(input('Quantas letras deseja: '))
num_numeros = int(input('Quantos números deseja: '))
num_simbolos = int(input('Quantos simbolos: '))

# Randomizaçao das listas
caracteres.append(random.choices(letras, k=num_letras))
caracteres.append(random.choices(numeros, k=num_numeros))
caracteres.append(random.choices(simbolos, k=num_simbolos))

# tranformando listas aninhadas numa lista unica e trocando ordem
for i in caracteres:
    for j in i:
        caracteres_ordem.append(j)
random.shuffle(caracteres_ordem)

# concatenando elementos da lista em uma 'string'
for i in caracteres_ordem:
    senha += i
print(f'Sua senha será: \n{senha}')
