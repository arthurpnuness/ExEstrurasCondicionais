## Write a Python algorithm that, given a person's age, determines their classification: adult or minor.

# User interaction
age = int(input('Enter your age: '))

# Conditional structures and result display
if age <= 18:
    print('You are a minor')
else:
    print('You are an adult')
