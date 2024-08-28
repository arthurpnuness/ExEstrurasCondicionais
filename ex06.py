## Read a number provided by the user. If the number is positive, display its double. If the number is negative, show a message saying that the number is invalid

# User interaction
num = float(input('Enter a number: '))

# Conditional structures, calculations, and result display
if num > 0:
    double = num * 2
    print('The number you entered is greater than 0, and its double is {}'.format(double))
else:
    print('The number you entered is invalid')
