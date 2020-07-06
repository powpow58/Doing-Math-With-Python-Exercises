'''
The unit conversion program we wrote in this chapter is limited 
to conversions between kilometers and miles. Try extending 
the program to convert between units of mass (such as kilograms 
and pounds) and between units of temperature (such as Celsius and 
Fahrenheit).
'''

def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

def km_miles():
    km = float(input("Enter distance in kilometers: "))
    miles = km / 1.609

    print("Distance in miles: {0}".format(miles))

def miles_km():
    miles = float(input("Enter distance in miles: "))
    km = miles * 1.609

    print("Distance in kilometers: {0}".format(km))

def kg_pounds():
    kg = float(input("Enter weight in kilograms: "))
    pounds = round((kg * 2.20462262185), 3)

    print("Weight in pounds: {0}".format(pounds))

def pounds_kg():
    pounds = float(input("Enter weight in pounds: "))
    kg = round((pounds * 0.45359237), 3)

    print("Weight in kilograms: {0}".format(kg))

def execute_program():
    while True:
        print_menu()
        choice = input("Which conversion would you like to do?: ")

        if choice == "1":
            km_miles()

        if choice == "2":
            miles_km()
        
        if choice == "3":
            kg_pounds()

        if choice == "4":
            pounds_kg()

        leave = input("Would you like to perform another action?\n").lower()
        if leave == "no":
            break