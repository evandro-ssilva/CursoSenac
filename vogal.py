#Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.


letra_digitada = input('Digite um caracter: ')
letra_digitada.casefold

if (letra_digitada == 'a') or (letra_digitada == 'e') or (letra_digitada == 'i') or (letra_digitada == 'u'):
    print('%s é uma vogal'%letra_digitada)

else:

    print('%s não é uma vogal'%letra_digitada)

