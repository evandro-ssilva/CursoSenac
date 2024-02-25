#Faça um algoritmo que verifica se um determinado valor é um número inteiro.

valor_digitado = input('Digite um valor: ')

try:
    if valor_digitado.isdigit():

        valor_digitado == int(valor_digitado)
        print(f'O numero {valor_digitado} é um número inteiro')

    else:

        valor_digitado = float(valor_digitado)
        print(f'O numero {valor_digitado} é um número decimal')

except ValueError: 

    print('O valor informado não é um número: ')

