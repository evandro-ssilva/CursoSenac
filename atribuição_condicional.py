num = input("digite um número: ")
try:
    a = int(num) if num.isdigit() else float(num)

    print(a,type(a))

except ValueError:

    print('Você não digitou um número')

