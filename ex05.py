## Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação: maior de idade ;menor de idade;

idade = int(input('Digite sua idade: '))

if idade <= 18:
    print('Voce é menor de idade')
else:
    print('Voce ja é maior de idade')