# Faça um algoritmo que solicite ao usuário informar 3 números. 
# Em seguida, some-os e envie para a saída padrão a seguinte frase: 
# "A soma total é: "


first_number = float (input('Digite um número: '))
second_number = float (input('Digite um segundo número: '))
thirth_number = float (input('Digite o ultimo número: '))

soma = first_number + second_number + thirth_number

print(f'A soma total é: {soma:.1f}')