from matplotlib import pyplot as plt
import math 

def fibo(n):
    if n == 1:
        return [1]
    
    if  n == 2:
        return [1, 1]

    # n > 2
    a = 1
    b = 1

    # First two members of the series
    series = [a, b]
    for  i in range(n):
        
        c = a + b

        series.append(c)

        a = b
        b = c
    gratio = [ series[i] / float(series[i - 1]) for i in range(len(series))]
    
    draw_graph(series, gratio)

def draw_graph(series, gratio):
    xseries = list(range(len(series)))

    plt.plot(xseries, gratio)
    plt.xlabel("No.")
    plt.ylabel("Ratio")
    plt.title("Ratio between consecutive Fibonacci numbers")
    plt.show()

def execute_program():
    fibo(100)