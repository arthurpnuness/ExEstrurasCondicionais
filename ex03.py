## Create an algorithm that reads a person's year of birth and checks whether they are eligible to vote (disregard the birth month).

# User interaction
yearOfBirth = int(input('Enter your year of birth: '))

# Conditional structures and result display
if yearOfBirth <= 2006:
    print('Congratulations, you are eligible to vote!')
else: 
    print('Unfortunately, you are not old enough to vote. :(')
