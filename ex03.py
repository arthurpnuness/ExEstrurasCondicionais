## Faça um algoritmo que leia o ano de nascimento de uma pessoa e verifique se ela pode ou não votar (desconsidere o mês de nascimento).

ano = int(input('Digite o ano do teu nascimento: '))

if ano <= 2006:
    print('Parabens voce já pode votar!')
else: 
    print('Infelizmente voce nao tem idade suficiente para votar :( ')