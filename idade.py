'''Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. 
Em seguida, imprima na tela com quantos anos sua mãe o teve.'''


idade_usuario = int(input('Digite a sua idade: '))
idade_mae = int(input('Digite a sua idade: '))

idade_gestação = None

if idade_mae >= (idade_usuario + 13): # valor para inferir se a mulher poderia engravidar
    idade_gestação = idade_mae - idade_usuario
    print('A sua mãe o teve com %d'%idade_gestação)
else:
    print('Dados não conferem,\na idade minima para uma mulher engravidar é 13 anos')