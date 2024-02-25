'''
escreva um algoritmo que peça um numero inteiro e informe ao
usuário se o numero é inteiro ou não

'''

numero_digitado = int(input('Digite um número inteiro: '))

positivo_negativo = 'numero [Positivo]' if numero_digitado >= 0 else 'numero [Negativo]'

print(f'{numero_digitado} é {positivo_negativo}')