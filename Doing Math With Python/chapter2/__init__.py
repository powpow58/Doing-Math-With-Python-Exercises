from chapter2.How_Does_the_Temperature_Vary_During_the_Day.program import execute_program as ex1
from chapter2.Explorig_the_Relationship_Between_the_Fibonacci_Sequence_and_the_Golden_Ratio.program import execute_program as ex2
from chapter2.Enhaced_Projectile_Trajectory_Comparison_Program.program import execute_program as ex3
from chapter2.Visualizing_Your_Expenses.program import execute_program as ex4
from chapter2.Explorig_the_Relationship_Between_the_Fibonacci_Sequence_and_the_Golden_Ratio.program import execute_program as ex5
from addon_code.console import screen_clear as clear

def first():
    ex1()

def second():
    ex2()

def third():
    ex3()

def forth():
    ex4()

def fifth():
    ex5()

options = { 0: first,
            1: second,
            2: third,
            3: forth,
    }

def Chapter2_Menu():
    print("Select an exercise")
    print("1. Enhaced Projectile Trajectory Comparison Program")
    print("2. Explorig the Relationship Between the Fibonacci Sequence and the Golden Ratio")
    print("3. Exploring a Quadratic Function Visually")
    print("4. Visualizing_Your_Expenses")
    print("5. How Does the Temperature Vary During the Day")

    num = int(input())
    options[num]()

    clear()

    
