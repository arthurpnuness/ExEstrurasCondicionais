## Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde  h corresponde a altura): Homens: (72.7 ∗ h) − 58 / Mulheres: (62, 1 ∗ h) − 44, 7

altura = float(input('Qual a sua altura: '))
sexo = input('Voce se identifica pelo genero masculino ou feminino? ')

if sexo == "masculino":
    pecoIdeal = (72.7 * altura) - 58
    print('O teu peso ideal é {}'.format(pecoIdeal))
else:
    pecoIdeal = (62.1 * altura) - 44.7
    print('O teu peso ideal é {}'.format(pecoIdeal))
