''' 
Quadratic function calculator
'''
from matplotlib import pyplot as plt
def drawgraph():
    # Assume values of x
    x_values = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_values = []

    for x in x_values:

        # Calculate the value of the quadratic function
        y = x ** 2 + 2 * x + 1

        y_values += [y]

        print("x = {0} y = {1}".format(x, y))

    plt.title("Quadratic Function Graph")
    plt.xlabel("x-variable")
    plt.ylabel("y-variable")
    plt.plot(x_values, y_values, marker="o")
    plt.show()

def execute_program():
    drawgraph()