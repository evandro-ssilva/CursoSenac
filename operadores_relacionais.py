'''
escreva um algoritmo que receba um valor idade
baseado no valor da idade informe se o usuario é maior de idade
o intervalo para a maior idade deve ficar entre 18 e 150

'''

idade_usuario = int(input('Digite a sua idade em numero de anos: '))

if idade_usuario >= 18 and idade_usuario <=150:

    print(f'{idade_usuario} é maior de idade')


else:

    if idade_usuario < 18 :

        print(f'{idade_usuario} este usuário é menor de idade')

    else:

        print(f'{idade_usuario} [matusalém]')

