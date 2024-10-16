#QUESTION 4: Simple Functions
#Objective: Write and use functions.
#Instructions: Write a function that takes two numbers as parameters and returns their greatest common divisor (GCD).
# Test the function with different inputs.
import math


def gcd_numbers(x, y):
    if y == 0:
        return x
    else:
        return gcd_numbers(y, x%y)

#Input numbers to determine GCD;
number1 = int(input("Enter first Number: "))
number2 = int(input("Enter Second Number: "))

#Find the output of the 2 numbers.
print(gcd_numbers(number1,number2))
print('-'*30)
#OR:

#Using Maths Methods;
def compute_gcd(a, b):
    return math.gcd(a, b)

#Testing the functions with different input:
gcd_inpute = compute_gcd(48, 18)

#Find the Output
print(gcd_inpute)



