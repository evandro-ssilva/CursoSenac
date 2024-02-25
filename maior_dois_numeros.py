number1 = int(input('Digite o primeiro numero da comparação: '))
number2 = int(input('Digite o segundo numero da comparação: '))
maior_numero = None

if number1 > number2 :

    maior_numero = number1
    print('%d é maior que %d'%(number1,number2))

else:
    maior_numero = number2
    print('%d é maior que %d'%(number2,number1))