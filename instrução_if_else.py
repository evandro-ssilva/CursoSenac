'''
escreva um algoritmo que receba um valor e armazene em uma variavel
o programa deve responder com o numero da opção e caso o usuario escolha
uma opção que não foi pedida informar que não é valido

'''
ação = int(input("Digite '1' ou '2' : "))

if (ação == 1) or (ação == 2):

    print(f'A opção escolhida foi a nº {ação}')

else: 

    print(f'a opção {ação} não é valida')
