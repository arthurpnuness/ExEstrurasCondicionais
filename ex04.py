## A driver wants to put X amount of money into their gas tank. Write an algorithm to read the price per liter of gasoline and the payment amount, and display how many liters they were able to put in the tank.

gasolinePrice = 6.00  # This is where the gasoline price was defined
payment = int(input('How much would you like to spend on fuel? '))  # User interaction

# Calculation
liters = payment / gasolinePrice

# Display the result
print('The amount of fuel filled was {} liters'.format(liters))



