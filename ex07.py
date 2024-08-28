## Create a program that receives a person's height and gender and calculates and displays their ideal weight, using the following formulas (where h corresponds to height): Men: (72.7 * h) - 58 / Women: (62.1 * h) - 44.7

# User interaction
h = float(input('What is your height? '))
gender = input('Do you identify as male or female? ')

# Conditional structures, calculations, and result display
if gender == "male":
    idealWeight = (72.7 * h) - 58
    print('Your ideal weight is {}'.format(idealWeight))
else:
    idealWeight = (62.1 * h) - 44.7
    print('Your ideal weight is {}'.format(idealWeight))
