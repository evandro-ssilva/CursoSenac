'''
Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros
que estejam associados a uma chave. 
Em seguida, imprima na tela o nome da chave e o respectivo valor:
'''

def dicionario(**args):

    print(args)

dicionario(azul = 1, vermelho = 2)


