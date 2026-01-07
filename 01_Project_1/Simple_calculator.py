'''
Don't judge because it's my first python project 
My first project of python 
project name -  Basic Calculator (only can do + , - , * , / )
'''

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("Addition:", number1, "+", number2, "=", number1 + number2)
print("Subtraction:", number1, "-", number2, "=", number1 - number2 )
print("Multiplication:", number1, "*", number2, "=", number1 * number2 )

if number2 != 0:
    print("Division:", number1, "/", number2, "=", number1 / number2)
else:
    print("Division is not possible (division by zero)")

