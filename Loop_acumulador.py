'''
Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. 
Em seguida, calcule e envie para a saída padrão a média:

'''
i = 0
acumulador = 0


while i < 4 :

    nota = int(input('Digite a nota do Aluno: '))
    acumulador += nota
    i += 1
media = acumulador / 4
print(f'A media é igual a : ' + str(media))
