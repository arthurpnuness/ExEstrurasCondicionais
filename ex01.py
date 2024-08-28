## Faça um algoritmo para calcular o salário mensal de um funcionário. Sabe-se que o funcionário recebe R$35,00 por hora, faça um algoritmo que leia o total de horas trabalhadas no mês e apresente o salário final. Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido, senão apresente somente o resultado da multiplicação.

valorHora = 35
horasTrabalhadas = int(input('Digite quantas horas tu trabalhou: '))

salarioFinal = valorHora * horasTrabalhadas

if salarioFinal <= 1000:
    aumento = salarioFinal + 300
    print('Como voce recebe menos de R$1.000,00 receberá um aumento de R$300,00 Parabens!')
else:
    print('Voce recebe R${} por mês'.format(salarioFinal))
 