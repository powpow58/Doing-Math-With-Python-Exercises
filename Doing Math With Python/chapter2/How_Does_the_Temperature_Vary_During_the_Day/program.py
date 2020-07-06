''' 
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt

def draw_graph(times , sweden_temp_list, trinidad_temp_list):
    xtimes = list(range(len(times)))

    # Plot points on graph
    plt.plot(xtimes, sweden_temp_list, xtimes, trinidad_temp_list, marker="o")

    # Give label to x-axis
    plt.xlabel("Time of Day")

    # Give label to y-axis
    plt.ylabel("Tempreture (℃)")

    # Give title to Graph
    plt.title("Comparison of Trinidad & Sweden's Weather")

    #Setting up the y-axis minimum
    plt.axis(ymin = -0)

    plt.xticks(xtimes, times)

    # Add a legend and show the graph
    plt.legend(["Sweden", "Trinidad"])

    # Show graph
    plt.show()


def execute_program():
    # List of temperatures of different hours in Sweden
    sweden_temp_list = [3, 2, 2, 2, 2, 2, 2, 2]

    # List of temperatures of different hours in Trinidad
    trinidad_temp_list = [23, 23, 23, 23, 23, 23, 25, 27]

    times = ([ "{0} : 00 AM". format(x) for x in range(2, 10, 1)])

    draw_graph(times, sweden_temp_list, trinidad_temp_list)
    
