## Leia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do valor digitado. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

num = float(input('Digite um numero: '))

if num > 0:
    dobro = num * 2
    print('O numero que voce digitou é maior que 0 e o dobro dele é {}'.format(dobro))
else:
    print('O numero que voce digitou é inválido')