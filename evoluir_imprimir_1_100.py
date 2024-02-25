'''
Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido
para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:

 '''
resultado = []
inicio = int(input('Digite o numero no qual o loop vai começar a impressão: '))
fim = int(input('Digite o numero no qual o loop vai parar a impressão: '))
passo = int(input('Digite o intervalo que vai definir a distância de impressão entre os numeros ex: 1 à 1: '))


for i in range(inicio,(fim + 1),passo):

    resultado.append(i)

print(f'O pedido foi para imprimir de {inicio} até {fim}\n{resultado}')

