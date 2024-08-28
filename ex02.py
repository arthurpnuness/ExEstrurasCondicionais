## Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 <= num2:
    print('A ordem crescente dos numeros digitados é {} - {}'.format(num1, num2))
else:
    print('A ordem crescente dos numeros digitados é {} - {}'.format(num2, num1))