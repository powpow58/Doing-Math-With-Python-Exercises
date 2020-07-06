'''
Write a calculator that can perform the basic mathematical operations 
on two fractions. It should ask the user for two fractions and 
the operation the user wants to carry out.
'''

from fractions import Fraction

def add(a, b):
    print("Result of Addition: {0}".format(a + b))

def subtract(a, b):
    print("Result of Subtraction: {0}".format(a - b))

def divide(a, b):
    print("Result of Division: {0}".format(a / b))

def multiply(a, b):
    print("Result of Multiplication: {0}".format(a * b))

def execute_program():
    while True:
        a = Fraction(input("Enter first fraction: "))
        b = Fraction(input("Enter second fraction: "))
        op = input("Operation to perform - Add, Subtract, Divide, Multiply: ").lower()
        
        if op == "add":
            add(a, b)
        
        if op == "subtract":
            subtract(a, b)

        if op == "divide":
            divide(a, b)
        
        if op == "multiply":
            multiply(a, b)

        leave = input("Would you like to perform another action?\n").lower()
        if leave == "no":
            break