# Python Demo 3B
# Mr. Scott
# May 24, 2022
# Is Mr. Scott getting old...?


def cleaning(hair_choice):
    # depending on the hair choice, print out a message
    # Billy Madison reference to age myself... 
    if hair_choice.lower() == "shampoo":
        print("Shampoo is better")
    elif hair_choice.upper() == "CONDITIONER":
        print("Conditioner is better")
    else:
        print("Stop Staring at me Swan")


    
print("Welcome to the hair treatment simulator")
choice = input("What hair product would you like? ")
cleaning(choice)

# String Methods
# for any string or string variable:
#     .upper() → returns string as all uppercase characters
#     .lower() → returns string as all lowercase characters
#     .capitalize() → returns string, lowercase except 1st char

#     = → variable assignment
#     == → equality comparison