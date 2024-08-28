## Create an algorithm that reads two distinct numbers and displays them in ascending order.

# User interaction
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

# Conditional structures and result display
if num1 <= num2:
    print('The ascending order of the numbers entered is {} - {}'.format(num1, num2))
else:
    print('The ascending order of the numbers entered is {} - {}'.format(num2, num1))
