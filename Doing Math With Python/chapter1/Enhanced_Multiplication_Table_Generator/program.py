'''
    Our multiplication table generator is cool, but it prints only the first 
    10 multiples. Enhance the generator so that the user can specify both the 
    number and up to which multiple. For example, I should be able to input 
    that I want to see a tbale listhig the first 15 multiples of 9.
'''

def multi_table(multiple, number_of_multiples):
    for i in range(number_of_multiples + 1):
        answer = multiple * i
        print("{0} x {1} = {2}".format(multiple, i, answer))

def execute_program():
    while True:
        multiple = input("What number would you like to know the multiples of?\n")
        number_of_multiples = input("How many multiples would you like?\n")
        try:
            multi_table(int(multiple), int(number_of_multiples))
        except ValueError:
            try:
                val = float(number_of_multiples)
                print("Input is a float number")
            except ValueError:
                print("Input is not a number. It's a string")
                
        leave = input("Would you like to perform another action?\n").lower()
        if leave == "no":
            break

