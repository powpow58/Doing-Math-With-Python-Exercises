'''
Try writing an “even-odd vending machine,” which will take a number 
as input and do two things:

1. Print whether the number is even or odd.
2. Display the number followed by the next 9 even or odd numbers.

    If the input is 2, the program should print even and then 2, 4, , 8, 10, 12, 
14, 16, 18, 20. Similarly, if the input is 1, the program shold print odd and 
then print 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.

    Your program should use the is_integer() method to display an error message 
    if the input is a number with significant digits beyond the decimal point. 

'''

def even_odd(number):
    if (number % 2) == 0:
            print("even")
            for i in range(number + (number + 18)):
                if (i % 2) == 0:
                    print(i)
    else:
        print("odd")
        for i in range(number + (number + 18)):
            if (i % 2) == 1:
                print(i)

def execute_program():
    while True:
        number = float(input("Type a number:\n"))
        if number.is_integer() == True:
            even_odd(int(number))
        else:
            print("The entered number is not an integer")
                
        leave = input("Would you like to perform another action?\n").lower()
        if leave == "no":
            break
        