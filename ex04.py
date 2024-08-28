## Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

precoGasolina = 6.00
pagamento = int(input('Quantos o senhor deseja abastecer: '))

litros = pagamento / precoGasolina

print('A quantidade de litros abastecida foi de {}'.format(litros))


