'''
Faça um algoritmo que leia um número e mostre se o mesmo 
é positivo, negativo ou zero.

'''

num = int(input('Digite um número: '))

if (num > 0):
    print('%d é positivo'%num)
elif (num < 0):
    print('%d é negativo'%num)
elif (num == 0):
    print('%d é igua a zero'%num)

