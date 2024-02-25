'''
Escreva uma função que verifica se uma String enviada é um palíndromo ou não.

'''


def palindro(abc):

    abc_reverso = abc[-1::-1]

    if abc == abc_reverso:

        print(f'{abc} é palindromo')
    else:
        print(f'{abc} não é palindromo')
  


    
palindro('coco')
      
