'''
Faça um algoritmo que some
a quantidade de números pares encontrados 
no intervalo entre 0 e 100:

'''

soma = 0

for i in range(101):

    if i % 2 == 0:
        soma += i
        print(f'Os numeros pares são {i} a soma = {soma}')