'''
 Faça um algoritmo que solicite ao usuário informar o valor de uma compra. 
 Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total
 e também o valor com o desconto aplicado.

'''

custo_da_compra = float(input('Digite o valor da compra: '))

try:

    desconto = (custo_da_compra * 10) / 100

    valor_com_desconto = custo_da_compra - desconto
    
    print(f'O valor total sem desconto é: {custo_da_compra}\nO valor com desconto de [10%] é: {valor_com_desconto}')
except:

    print('Erro, tente novamente')
    