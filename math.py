print('\nWelcome to my simple math python program')
print('I wrote this python program inside of termux')
print('This python program is being interpreted and run inside of termux')
print('Enter 2 numbers when asked and it will be solved using arithmetic')

#ask user
num1 = int(input('\nEnter 1st number: '))
num2 = int(input('Enter 2nd number: '))

#operation
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

#display
print(f'\nSum: {sum}')
print(f'Difference: {difference}')
print(f'Product: {product}')
print(f'Quotient: {quotient}')
