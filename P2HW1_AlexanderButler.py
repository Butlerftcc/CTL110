# A program that calculates travel expenses
# 9/5/23
# CTI-110 P1HW2 - Travel Expense
# Alexander Butler

#Ask user to enter their budget
#Ask user to enter travel destination
#Ask user for amount they will spend on gas
#Ask user for amount they will spend on accommodation
#Ask user for amount they will spend on food
#Add expenses
#Subtract expenses from budget
#Display results

print('This program calculates and displays tarvel expenses.\n')
Budget = float(input('Enter Budget: '))
Destination = input('\nEnter your travel destination: ')
Gas = float(input('\nHow much do you think you will spend on gas? '))
Accomodation = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
Food = float(input('\nLast, how much do you need for food? '))
Expenses = Gas + Accomodation + Food
RemainBudget = Budget - Expenses

print('-----------Travel Expenses-----------')
print('Location:', '          ' f'{Destination}')
print('Initial Budget:', '    ' f'${Budget}')
print('Fuel:', '              ' f'${Gas}')
print('Accomodation:', '      ' f'${Accomodation}')
print('Food:', '              ' f'${Food}')
print('-------------------------------------\n')
print('Remaining Balence:', ' ' f'${RemainBudget}')
