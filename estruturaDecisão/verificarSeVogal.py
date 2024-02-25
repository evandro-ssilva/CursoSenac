'''
Faça um Programa que verifique se uma letra digitada
é vogal ou consoante.

'''
lista_vogal = ['A','E','I','O','U']

entrada_usuario = input('Digite um character para a verificação do tipo: ')

entrada_verificação = entrada_usuario.upper()

tipo_caracter = 'vogal' if entrada_verificação in lista_vogal else 'não vogal'

print(f'{entrada_verificação} é um charactere [{tipo_caracter}]')

