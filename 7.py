# 7. Write a Python program that prompts the user for a number and then checks if the number
# is even or odd. Print an appropriate message based on the result.
num = int(input('Enter number : '))
if num % 2 == 0:
    print('Even')
elif num % 2 != 0:
    print('odd')
else:
    print('invalid num')
