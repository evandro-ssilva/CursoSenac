'''
Escreva um função que some todos os números contidos numa lista.
Lista: (1, 2, 3, 4, 5)
Soma: 15

'''
lista = [1,2,3,4,5]

def somar_lista(x):
    soma = 0
    for i in lista :
         soma += i
         
    return soma    
result = somar_lista(lista)

print(result)
    


    

