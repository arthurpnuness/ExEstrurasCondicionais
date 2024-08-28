## Create an algorithm to calculate an employee's monthly salary. It is known that the employee earns R$35.00 per hour. Create an algorithm that reads the total hours worked in the month and displays the final salary. If the salary is less than R$1,000.00, give a R$300.00 raise to the received salary; otherwise, display only the result of the multiplication

hourlyRate = 35  # This is where the hourly rate was defined
hoursWorked = int(input('Enter the number of hours you worked: '))  # Interaction with the user

# Calculation
finalSalary = hourlyRate * hoursWorked

# Conditional structures and result display
if finalSalary <= 1000:
    raiseAmount = finalSalary + 300
    print('Since you earn less than R$1,000.00, you will receive an increase of R$300.00. Congratulations!')
else:
    print('You earn R${} per month'.format(finalSalary))

 
