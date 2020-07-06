from chapter1.Even_Odd_Vending_Machine.program import execute_program as ex1
from chapter1.Enhanced_Multiplication_Table_Generator.program import execute_program as ex2
from chapter1.Enhanced_Unit_Converter.program import execute_program as ex3
from chapter1.Fraction_Calculator.program import execute_program as ex4
from addon_code.console import screen_clear as clear


def first():
    ex1()

def second():
    ex2()

def third():
    ex3()

def forth():
    ex4()

options = { 1: first,
            2: second,
            3: third,
            4: forth,
    }

def Chapter1_Menu():
    print("Select an exercise")
    print("1. Even - Odd Vending Machine")
    print("2. Enhanced Multiplication Table Generator")
    print("3. Enhanced Unit Converter")
    print("4. Fraction Calculator")

    num = int(input())
    options[num]()

    clear()

    