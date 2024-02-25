'''
Faça um algoritmo em que o usuário informe uma medida em metros. 
Em seguida, converta essa medida para centímetros
 e envie para a saída padrão:

'''

medida_usario = float(input('Digite a medida em [Centimetros]: '))

medida_em_centimetro = medida_usario * 100

print(f'{medida_usario} metro equivale à {medida_em_centimetro} centimetro')