'''
Faça um Programa que peça dois números
e imprima o maior deles.

'''
numero_um = int(input('Digite um número inteiro: '))
numero_dois = int(input('Digite um número inteiro: '))

maior_numero = numero_um if numero_um > numero_dois else numero_dois

print(f'O maior número entre {numero_um} e {numero_dois} é o numero [{maior_numero}]')