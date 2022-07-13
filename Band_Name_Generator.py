# 1. Create a greating for your program.
# 2. Ask the User for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band new name.
# 5. Make sure the input cursor shows on a new line.

# Definindo variaiveis.
a = 'Qual o nome da cidade onde nasceu?\n'
b = 'Qual o nome do seu animal de estimação?\n'

# Criando uma saudação.
print('Bem vindo(a) ao gerador de nomes de bandas!')

# Criando input e armazenando dados nas variaveis.
a = input(a)
b = input(b)

# Resultado da criação do nome da banda.
print('O nome da sua banda pode ser ' + b + ' ' + a)
