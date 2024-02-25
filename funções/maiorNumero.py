'''
Escreva um algoritmo que encontre o maior dentre 3 números.
Para facilitar a resolução do exercício utilize funções.

'''


def numero_maior(x,y,z):

    if x > y and x > z:
        print(f'[{x}] é o maior numero entre {x}, {y} e {z}')
    elif z > x and z < y:
        print(f'[{z}] é o maior numero entre {x}, {y} e {z}')
    elif y > x and y < z:
        print(f'[{y}] é o maior numero entre {x}, {y} e {z}')
    
numero_maior(3,2,1)