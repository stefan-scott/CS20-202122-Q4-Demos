# Python Day Three Demo
# Mr. Scott
# May 24th, 2022
# Demo on:  try-except, functions, is mr.scott getting old

# DEMO ONE → user input, exceptions, handling errors


def add_numbers():  # function signature
    # get two values from user, print out their sum
    while True:
        try:
            number_one = input("Enter a number: ")
            number_one = int(number_one)  #CAN CRASH
            break
        except:
            print("That's not a number!! Try Again...")
        
        
    number_two = int(input("Enter a number: "))  #CAN CRASH
    
    result = number_one + number_two  
    
    print(result)

add_number()
