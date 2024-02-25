'''
Faça um algoritmo que imprima a frase "estou em looping"
e, em seguida, solicite ao usuário digitar uma letra.
 Caso a letra seja o "q" finalize a aplicação. Do contrário, 
imprima novamente a mesma frase até que o caractere "q" seja enviado:

'''

while True:

    print('"estou em looping"')

    op = input('Digite [q] - para encerrar ou qualquer outra para continuar: ')

    if op == 'q':

        print('não mais estou em loopin, fim!')

        break



