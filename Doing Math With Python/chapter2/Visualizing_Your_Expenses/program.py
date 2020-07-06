'''
Example of drawing a horizontal bar chart
'''

from matplotlib import pyplot as plt

def create_bar_chart(data, labels):
    
    # Number of bars
    num_bars = len(data)

    # This is list is the point on your y-axus where each
    # Bar is centered.  Here it will be [1, 2, 3...]
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align = 'center')
    
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly Expenditures')

    # Turns o the grid which may assit i visual estimation
    plt.grid()
    plt.show()

def execute_program():
    # Number of steps I walked during the past week
    steps = [6534, 7000, 8e900, 10786, 3467, 11045, 5095]

    try:
        number_of_categories = int(input("Enter number of categories: "))

        category_name = []
        category_expenditure = []

        for i in range(1, (number_of_categories + 1)):
            name = input("Enter name for category {0}: ".format(i))
            expenditure = int(input("Enter Category {0} expenditure: ".format(i)))

            name = name.capitalize()

            category_name.append(name)
            category_expenditure.append(expenditure)

        # Corresponding days
        labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        create_bar_chart(category_expenditure, category_name)
    except ValueError:
        print("Enter valid number")

    
    

    