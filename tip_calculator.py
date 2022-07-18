# Caluladora de gorjetas

print('Calculador de Gorjetas')
total = float(input('Qual o total a pagar: R$'))
gorjeta = int(input('Qual porcentagem você quer pagar: 10, 12 or 15?'))
numero_a_dividir = int(input('Quantas pessoas para dividir: '))

gorjeta_porcentagem = (gorjeta/100) + 1
total_mais_gorjeta = total * gorjeta_porcentagem
divisão_total = total_mais_gorjeta / numero_a_dividir

print(f'Cada pessoa deve pagar: R${divisão_total:.2f}')
