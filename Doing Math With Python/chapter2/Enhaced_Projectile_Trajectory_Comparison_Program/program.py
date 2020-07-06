'''
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):

    plt.plot(x, y)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title("Projectile motion of a ball")

def frange(start, final, interval):

    numbers = []
    
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

def draw_trajectory(u, theta):
    
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g

    print("Time of Flight: {0}".format(t_flight))

    # Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []

    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)

    sorted_x = sorted(x, reverse=True)
    print("Maximum Vertical Distance: {0}".format(sorted_x[0]))

    sorted_y = sorted(y, reverse=True)
    print("Maximum Horizontal Distance: {0}".format(sorted_y[0]))

    draw_graph(x, y)


def execute_program():
    try:
        number_of_trajectories = int(input("How many trajectories?\n"))
        trajectories = 1
        while trajectories < (number_of_trajectories + 1):
            u = float(input("Enter the initial velocity (m/s) of trajectory {0}: ".format(trajectories)))
            theta = float(input("Enter the angle of projection (degrees) of trajectory {0}: ".format(trajectories)))
            draw_trajectory(u, theta)

            trajectories += 1
        plt.show()
        

    except ValueError:
        print("You entered an invalid input")
