'''
Escreva uma função que imprima somente os números pares
Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Saída: [2, 4, 6, 8]

'''

def par(lista):

    lista_pares = []

    for i in lista:

        if i % 2 != 0:
            continue
        else:
            lista_pares.append(i)
    return lista_pares

resultado = par([1,2,3,4,5,6,7,8,9])
print(resultado)